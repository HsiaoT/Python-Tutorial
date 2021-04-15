
# The method works by examining each set of adjacent elements in the string, 
# from left to right, switching their positions if they are out of order. 
# The algorithm then repeats this process until it can run through the entire 
# string and find no two elements that need to be swapped.


# Time complexity (average): O(n^2)
# Time complexit (best): O(n) (list already sorted)
# Space complexity: O(1)

import random
init_random_Data = random.sample(range(100), 10)
print("Init list:")
print(init_random_Data)

def bubble_sort(nums):
	for i in range(len(nums)-1, 0, -1):
		flag = True
		for j in range(0, i):
			if nums[j]>nums[j+1]:
				flag = False
				nums[j], nums[j+1] = nums[j+1], nums[j]
		if flag:
			return nums
	return nums


sorted_Data = bubble_sort(init_random_Data)
print("\nsorted list:")
print(sorted_Data)









