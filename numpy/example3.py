
# -*- coding: utf-8 -*-

import numpy as np

# np.where
# np.unique



obj_ids_list = [0,1,2]
obj_ids = np.array(obj_ids_list)

mask_list = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 2, 2, 0]]
mask = np.array(mask_list)

masks = (mask == obj_ids[:,None, None])
print(masks)
# [[[ True  True  True  True]
#   [ True False False  True]
#   [ True False False  True]]

#  [[False False False False]
#   [False  True  True False]
#   [False False False False]]

#  [[False False False False]
#   [False False False False]
#   [False  True  True False]]]
print("")
for i in range(len(obj_ids)):
	pos = np.where(masks[i])
	xmin = np.min(pos[1])
	xmax = np.max(pos[1])
	ymin = np.min(pos[0])
	ymax = np.max(pos[0])
	print(pos[1], pos[0])
	print("instance# " + str(i), [xmin, ymin, xmax, ymax])
	print("")

