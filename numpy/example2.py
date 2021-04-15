
# -*- coding: utf-8 -*-

import numpy as np

# Q1
# Give a 4x4 array, please rotate the array as below
# ===================================================
matrix = np.arange(1,17).reshape(4,4)
# print(matrix)
# [[ 1  2  3  4],
#  [ 5  6  7  8],
#  [ 9 10 11 12],
#  [13 14 15 16]]
# ---->
# [[16 15 14 13],
#  [12 11 10  9],
#  [ 8  7  6  5],
#  [ 4  3  2  1]]
matrix_flat = matrix.flatten()
matrix_reversed = matrix_flat[::-1]
result = matrix_reversed.reshape(4,4)
# print(result)


# Q2
# multiple 2 array (numpy list)
# ===================================================
A = np.arange(9).reshape(3,3)
B = np.arange(10,19).reshape(3,3)
result = A.dot(B)
# print(result)

# Q2
# multiple 2 array (not numpy list)
# ===================================================
A = [[0,1,2],
     [3,4,5],
     [6,7,8]]
B = [[10,11,12],
     [13,14,15],
     [16,17,18]]
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			C[i][j] += A[i][k]*B[k][j]
# print(result == C)

# Q3
# transpose an array
# ===================================================
A = [[0,1,2],
     [3,4,5],
     [6,7,8]]
transpose = np.transpose(A)
# print(transpose)

A = [[0,1,2],
     [3,4,5],
     [6,7,8]]
# print(A.T)    # AttributeError: 'list' object has no attribute 'T'
A_npArray = np.array(A)
A_npArray.T
# print(A_npArray)

# Q4
# stack array
# ===================================================
A = [[0,1,2],
     [3,4,5]]
B = [[6,7,8],
     [9,10,11]]

V = np.vstack((A,B))
print(V)
H = np.hstack((A,B))
print(H)













