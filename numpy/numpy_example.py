
# -*- coding: utf-8 -*-

import numpy as np

# ndim   維度
# shape。形狀
# dtype  數值類型

np1 = np.array([1,2,3])
print(np1.ndim, np1.shape, np1.dtype)  # 一維, 三個元素, int64


print("\n========\n")
# 矩陣相加
np1 = np.array([1, 2, 3])
np2 = np.array([4, 5, 6])
print(np1 + np2)


print("\n========\n")
# 改變維度
np1 = np.array([1, 2, 3, 4, 5, 6])
np2 = np1.reshape([2,3])  # 列x行
print(np2.ndim, np2.shape, np2.dtype)  # 一維, 三個元素, int64
print(np2)

print("\n========\n")
# index
np1 = np.array([1, 2, 3, 4, 5, 6])
np2 = np1.reshape([2,3])
print(np2)
print(np2[1,1])  # 5

print("\n========\n")
# 建立矩陣
np1 = np.zeros([3,2])
np2 = np.ones([3,2])
print(np1)
print(np2)

print("\n========\n")
# 加總
np1 = np.array([1, 2, 3, 4, 5, 6])
np2 = np1.reshape([2,3])
print(np2)
print(np2.sum(axis=1))  # 橫向
print(np2.sum(axis=0))  # 縱向
