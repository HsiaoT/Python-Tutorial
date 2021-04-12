# -*- coding: utf-8 -*-
# refer to https://rowantseng.medium.com/%E4%BD%BF%E7%94%A8-pytorch-%E6%8F%90%E4%BE%9B%E7%9A%84%E9%A0%90%E8%A8%93%E7%B7%B4%E6%A8%A1%E5%9E%8B-pretrained-model-%E5%81%9A%E7%89%A9%E4%BB%B6%E5%81%B5%E6%B8%AC-object-detection-57ad9772a982

"""
pytorch.ipynb

Automatically generated by Colaboratory.

"""

# refer to https://www.mdeditor.tw/pl/pVEw/zh-tw
import torch
import torch.nn as nn
from torchvision import models
from torch.hub import load_state_dict_from_url

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# nn.AdaptiveAvgPool2d(output_size=(1,1)) -> input: (channels*H*W), output: (channnels*1*1)
# nn.AvgPool2d((7,7))
# load_state_dict_from_url
# load_state_dict
# torch.no_grad(): Disabling gradient to reduce calculation is useful for inference

# Step1 define new resnet18
# =====================================
class FullyConvolutionalResnet18(models.ResNet):
    def __init__(self, num_classes=1000, pretrained=False, **kwargs):

        # Start with standard resnet18 defined here 
        super().__init__(block = models.resnet.BasicBlock, layers = [2, 2, 2, 2], num_classes = num_classes, **kwargs)
        if pretrained:
            state_dict = load_state_dict_from_url(models.resnet.model_urls["resnet18"], progress=True)
            self.load_state_dict(state_dict)
        
        # change 1: Replace AdaptiveAvgPool2d with standard AvgPool2d
        # print("original avgpool: {}".format(self.avgpool))
        self.avgpool = nn.AvgPool2d((7, 7))
        # print("Replace with standard AvgPool2d:\n{}\n".format(self.avgpool))

        # chagne 2: Convert the original fc layer to a convolutional layer.
          # Define layer: last_conv and copy weight, bias from fc (orginal nesnet)  
        self.last_conv = torch.nn.Conv2d(in_channels = self.fc.in_features, out_channels = num_classes, kernel_size = 1)
        
          # self.fc.weight.data.shape = [1000, 512]
        self.last_conv.weight.data.copy_(self.fc.weight.data.view(*self.fc.weight.data.shape, 1, 1))
        self.last_conv.bias.data.copy_ (self.fc.bias.data)
          # self.last_conv.weight.data.shape = [1000, 512, 1, 1]
          # self.last_conv.bias.data.shape = [1000]

    # Reimplementing forward pass.
    # in torchvision/models/resnet, forward() will call _forward_impl()
    def _forward_impl(self, x):
        # Standard forward for resnet18
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)

        # Notice, there is no forward pass through the original fully connected layer. 
        # Instead, we forward pass through the last conv layer
        x = self.last_conv(x)
        return x

# Step2 apply new model with image
# =====================================
import torchvision.transforms as trns
import cv2

image_path = "/content/drive/MyDrive/Colab/image1.jpg"
mean = [0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
transforms = trns.Compose([trns.ToTensor(),
                           trns.Normalize(mean, std)])
original_image = cv2.imread(image_path)

from google.colab.patches import cv2_imshow
# resize image
dim = (600, 400)
original_image = cv2.resize(original_image, dim, interpolation = cv2.INTER_AREA)
cv2_imshow(original_image)
image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
image_tensor = transforms(image)           # [3,400,600]
image_tensor = image_tensor.unsqueeze(0)   # [1,3,400,600]

model = FullyConvolutionalResnet18(pretrained=True).eval()
# print(model)

with torch.no_grad():
  preds = model(image_tensor)
  preds = torch.softmax(preds, dim=1)
  print("Response map shape : ", preds.shape)  # original shape: (1,1000), now: (1,1000,1,2)

# from torchsummary import summary
# summary(model, (3, 387, 1024))
