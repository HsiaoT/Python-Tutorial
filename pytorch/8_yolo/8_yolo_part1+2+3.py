# -*- coding: utf-8 -*-
"""
pytorch.ipynb

Automatically generated by Colaboratory.

"""



# refer to https://blog.paperspace.com/how-to-implement-a-yolo-v3-object-detector-from-scratch-in-pytorch-part-2/

# !mkdir cfg/
# !cd cfg
# !wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg

"""
Convolutional
Shortcut
Upsample
Route
YOLO

Net
"""

from __future__ import division
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

def parse_cfg(cfgfile):
  """
  Takes a configuration file
  
  Returns a list of blocks. Each blocks describes a block in the neural
  network to be built. Block is represented as a dictionary in the list
  """
  file = open(cfgfile, "r")
  lines = file.read().split("\n")                        # store the lines in a list
  lines = [x for x in lines if len(x) > 0]               # get read of the empty lines 
  lines = [x for x in lines if x[0] != "#"]              # get rid of comments
  lines = [x.rstrip().lstrip() for x in lines]           # get rid of fringe whitespaces

  block = {}
  blocks = []

  for line in lines:
    if line[0] == "[":
      if len(block) != 0:
        blocks.append(block)
        block = {}
      block["type"] = line[1:-1].rstrip()
    else:
      key, value = line.split("=")
      block[key.rstrip()] = value.lstrip()
  blocks.append(block)
  return blocks

class EmptyLayer(nn.Module):
    def __init__(self):
        super(EmptyLayer, self).__init__()

class DetectionLayer(nn.Module):
    def __init__(self, anchors):
        super(DetectionLayer, self).__init__()
        self.anchors = anchors

# PyTorch has pre-built layers: Convolutional and Upsample
# we will have to write Shortcut, Route, YOLO
def create_modules(blocks):
  net_info = blocks[0]
  module_list = nn.ModuleList()
  
  prev_filters = 3     # track of number of filters in the layer on which the convolutional layer is being applied
  output_filters = []

  for index, x in enumerate(blocks[1:]):
    module = nn.Sequential()  # is used to sequentially execute a number of nn.Module objects.
    if(x["type"] == "convolutional"):
      activation = x["activation"]
      try:
        batch_normalize = int(x["batch_normalize"])
        bias = False
      except:
        batch_normalize = 0
        bias = True
      filters = int(x["filters"])
      padding = int(x["pad"])
      kernel_size = int(x["size"])
      stride = int(x["stride"])

      if padding:
        pad = (kernel_size - 1)//2
      else:
        pad = 0
      
      # Add the convolutional layer
      conv = nn.Conv2d(prev_filters, filters, kernel_size, stride, pad, bias=bias)
      module.add_module("conv_{0}".format(index), conv)

      # Add the batch norm layer
      if batch_normalize:
        bn = nn.BatchNorm2d(filters)
        module.add_module("batch_norm_{0}".format(index), bn)

      # Add activation
      # either Linear or Leaky ReLU for YOLO
      if activation == "leaky":
        activn = nn.LeakyReLU(0.1, inplace = True)
        module.add_module("leaky_{0}".format(index), activn)

    elif x["type"] == "upsample":
      stride = int(x["stride"])
      upsample = nn.Upsample(scale_factor = 2, mode = "bilinear")
      module.add_module("upsample_{}".format(index), upsample)
    
    elif x["type"] == "route":
      x["layers"] = x["layers"].split(",")

      # Start  of a route
      start = int(x["layers"][0])
      # End, if exists one
      try:
        end = int(x["layers"][1])
      except:
        end = 0
      
      if start > 0:
        start = start - index
      if end > 0:
        end = end - index
      route = EmptyLayer()
      module.add_module("route_{0}".format(index), route)
      if end < 0:
        #If we are concatenating maps
        filters = output_filters[index+start] + output_filters[index+end]
      else:
        filters = output_filters[index+start]
    
    elif x["type"] == "shortcut":
      shortcut = EmptyLayer()
      module.add_module("shortcut_{}".format(index), shortcut)

    elif x["type"] == "yolo":
      mask = x["mask"].split(",")
      mask = [int(m) for m in mask]
      
      anchors = x["anchors"].split(",")
      anchors = [int(a) for a in anchors]
      anchors = [(anchors[i], anchors[i+1]) for i in range(0, len(anchors), 2)]
      anchors = [anchors[i] for i in mask]

      detection = DetectionLayer(anchors)
      module.add_module("Detection_{}".format(index), detection)

    module_list.append(module)
    prev_filters = filters
    output_filters.append(filters)

  return (net_info, module_list)

# ==================================
# PART 2
# ==================================
def predict_transform(prediction, inp_dim, anchors, num_classes, CUDA=True):
  batch_size = prediction.size(0)
  stride =  inp_dim // prediction.size(2)
  grid_size = inp_dim // stride
  bbox_attrs = 5 + num_classes
  num_anchors = len(anchors)

  prediction = prediction.view(batch_size, bbox_attrs*num_anchors, grid_size*grid_size)
  prediction = prediction.transpose(1,2).contiguous()
  prediction = prediction.view(batch_size, grid_size*grid_size*num_anchors, bbox_attrs)
  
  anchors = [(a[0]/stride, a[1]/stride) for a in anchors]
  #Sigmoid the centre_X, centre_Y. and object confidencce
  prediction[:,:,0] = torch.sigmoid(prediction[:,:,0])
  prediction[:,:,1] = torch.sigmoid(prediction[:,:,1])
  prediction[:,:,4] = torch.sigmoid(prediction[:,:,4])

  #Add the center offsets
  grid = np.arange(grid_size)
  a,b = np.meshgrid(grid, grid)

  x_offset = torch.FloatTensor(a).view(-1,1)
  y_offset = torch.FloatTensor(b).view(-1,1)

  if CUDA:
      x_offset = x_offset.cuda()
      y_offset = y_offset.cuda()

  x_y_offset = torch.cat((x_offset, y_offset), 1).repeat(1,num_anchors).view(-1,2).unsqueeze(0)

  prediction[:,:,:2] += x_y_offset

  #log space transform height and the width
  anchors = torch.FloatTensor(anchors)

  if CUDA:
    anchors = anchors.cuda()

  anchors = anchors.repeat(grid_size*grid_size, 1).unsqueeze(0)
  prediction[:,:,2:4] = torch.exp(prediction[:,:,2:4])*anchors
  prediction[:,:,5: 5 + num_classes] = torch.sigmoid((prediction[:,:, 5 : 5 + num_classes]))
  prediction[:,:,:4] *= stride
  return prediction


class Darknet(nn.Module):
  def __init__(self, cfgfile):
    super(Darknet, self).__init__()
    self.blocks = parse_cfg(cfgfile)
    self.net_info, self.module_list = create_modules(self.blocks)

  # remember: self.blocks -> python List, self.module_list -> nn.ModuleList
  def forward(self, x, CUDA):
    modules = self.blocks[1:]
    outputs = {}
    write = 0
    
    for i, module in enumerate(modules):
      module_type = (module["type"])
      
      #---------------------- 
      if module_type == "convolutional" or module_type == "upsample":
        x = self.module_list[i](x)
      #----------------------
      elif module_type == "route":
        layers = module["layers"]
        layers = [int(a) for a in layers]
        if (layers[0] > 0):
          layers[0] = layers[0] - i
        if len(layers) == 1:
          x = outputs[i+(layers[0])]
        else:
          if(layers[1] > 0):
            layers[1] = layers[1] - i
          map1 = outputs[i+layers[0]]
          map2 = outputs[i+layers[1]]
          x = torch.cat((map1, map2), 1)
      #----------------------
      elif module_type == "shortcut":
        from_ = int(module["from"])
        x = outputs[i-1] + outputs[i+from_]
      #----------------------
      elif module_type == "yolo":
        anchors = self.module_list[i][0].anchors
        #Get the input dimensions
        inp_dim = int (self.net_info["height"])

        #Get the number of classes
        num_classes = int (module["classes"])

        #Transform 
        x = x.data
        x = predict_transform(x, inp_dim, anchors, num_classes, CUDA)
        if not write:              #if no collector has been intialised. 
          detections = x
          write = 1

        else:       
          detections = torch.cat((detections, x), 1)
      outputs[i]=x
    return detections


# ==================================
# PART 3
# ==================================
import cv2
!wget https://github.com/ayooshkathuria/pytorch-yolo-v3/raw/master/dog-cycle-car.png
def get_test_input():
    img = cv2.imread("dog-cycle-car.png")
    img = cv2.resize(img, (416,416))          # Resize to the input dimension
    img_ =  img[:,:,::-1].transpose((2,0,1))  # BGR -> RGB | H X W C -> C X H X W 
    img_ = img_[np.newaxis,:,:,:]/255.0       # Add a channel at 0 (for batch) | Normalise
    img_ = torch.from_numpy(img_).float()     # Convert to float
    img_ = Variable(img_)                     # Convert to Variable
    return img_

model = Darknet("yolov3.cfg")
inp = get_test_input()
print(model)
pred = model(inp, torch.cuda.is_available())
print (pred)
