# -*- coding: utf-8 -*-
"""opencv_test.ipynb

Automatically generated by Colaboratory.

"""

# cv2.calcHist: Histogram Calculation
# [image]
# [channel], 
# mask: None
# histSize: array of histogram sizes, 256
# ranges: value range, 0-256 

# cv2.split
# cv2.merge

# cv2.cvtColor
# cv2.imread
# cv2.imwrite

import cv2
import sys
import matplotlib.pyplot as plt

# Histogram Calculation for gray image
# ====================================== 
def calcHist_gray(img1):
  gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  hist = cv2.calcHist([gray], [0], None, [256], [0,256])
  plt.plot(hist)

# Histogram Calculation for RGB image
# ======================================
def calcHist_RGB(img1):
  color = ("B","G","R")
  for i, c in enumerate(color):
    hist = cv2.calcHist([img1], [i], None, [256], [0,256])
    plt.plot(hist, color=c)
    plt.xlim([0,256])

# Histogram Equalization for Gray image
# ======================================
def equalizeHist_gray(img1):
  gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  eq = cv2.equalizeHist(gray)
  hist = cv2.calcHist([eq], [0], None, [256], [0,256])
  cv2.imwrite(working_dir + "equalizeHist_gray.png",eq)
  plt.plot(hist)

def equalizeHist_RGB(img1):
  (B,G,R) = cv2.split(img1)
  eq_B = cv2.equalizeHist(B)
  eq_G = cv2.equalizeHist(G)
  eq_R = cv2.equalizeHist(R)
  res = cv2.merge([eq_B, eq_G, eq_R])
  cv2.imwrite(working_dir + "equalizeHist_RGB.png",res)

working_dir = "/content/drive/MyDrive/opencv/"
img1 = cv2.imread(working_dir + "image1.jpg")

calcHist_gray(img1)
calcHist_RGB(img1)
equalizeHist_gray(img1)
equalizeHist_RGB(img1)

#cv2.imwrite(working_dir + "output.png",img1)