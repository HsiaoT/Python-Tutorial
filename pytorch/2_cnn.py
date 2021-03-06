# -*- coding: utf-8 -*-
"""
pytorch.ipynb

Automatically generated by Colaboratory.

"""

import torch.nn as nn
import torch.nn.functional as F
import torch

batch_size = 2
one_hot_size = 10          # word vector size
sequence_width = 7         # sequence size
data = torch.randn(batch_size, one_hot_size, sequence_width)

conv1 = nn.Conv1d(in_channels=one_hot_size, out_channels=16, kernel_size=3)
conv2 = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=3)
conv3 = nn.Conv1d(in_channels=32, out_channels=64, kernel_size=3)

intermediate1 = conv1(data)
intermediate2 = conv2(intermediate1)
intermediate3 = conv3(intermediate2)

print(data.size())              # [2, 10, 7]
print(intermediate1.size())     # [2, 16, 5]
print(intermediate2.size())     # [2, 32, 3]
print(intermediate3.size())     # [2, 64, 1]

# Returns a tensor with all the dimensions of input of size 1 removed.
y_output = intermediate3.squeeze()
print(y_output.size())          # [2, 64]

print("=====================\n")

conv1_bn = nn.BatchNorm1d(num_features=16)

intermediate1 = conv1(data)
intermediate1_bn = conv1_bn(intermediate1)

print(data.size())
print(intermediate1.size())     # [2, 16, 5]
print(intermediate1_bn.size())  # [2, 16, 5], same size

print("=====================\n")
conv1_1x1 = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=1)

intermediate1 = conv1(data)
intermediate1_1x1 = conv1_1x1(intermediate1)

print(data.size())
print(intermediate1.size())     # [2, 16, 5]
print(intermediate1_1x1.size())  # [2, 32, 5], only channel changes
