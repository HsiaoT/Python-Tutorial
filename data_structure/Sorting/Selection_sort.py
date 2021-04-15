

# The selection sort algorithm sorts an array by repeatedly finding the 
# minimum element (considering ascending order) from unsorted part and 
# putting it at the beginning. The algorithm maintains two subarrays in a given array.

# Time complexity (average): O(n^2)
# Time complexit (best): O(n^2) (list already sorted)
# Space complexity: O(1)

import random
init_random_Data = random.sample(range(100), 10)
print("Init list:")
print(init_random_Data)

def selection_sort(nums):
	for i in range(len(nums)):
		min_index = i
		for j in range(i+1, len(nums)):        # Find the minimum 
			if nums[min_index] > nums[j]:
				min_index = j
		nums[i], nums[min_index] = nums[min_index], nums[i]
	return nums

sorted_Data = selection_sort(init_random_Data)
print("\nsorted list:")
print(sorted_Data)



