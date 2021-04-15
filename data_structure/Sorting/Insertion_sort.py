

# Insertion sort is a simple sorting algorithm that works 
# similar to the way you sort playing cards in your hands. 
# The array is virtually split into a sorted and an unsorted 
# part. Values from the unsorted part are picked and placed 
# at the correct position in the sorted part.

# [12, 11, 13, 5, 6]
# ->
# [12] [11, 13, 5, 6]
# [11, 12] [13, 5, 6]
# [11, 12, 13] [5, 6]
# [5, 11, 12, 13] [6]
# [5, 6, 11, 12, 13]

# Time complexity (average): O(n^2)
# Time complexit (best): O(n) (list already sorted)
# Space complexity: O(1)

import random
init_random_data = random.sample(range(100), 10)
print("Init list:")
print(init_random_data)

def insert_sort(nums):
	length = len(nums)
	for i in range(1, length):
		insert_value = nums[i]
		j = i -1

		while j >= 0:
			if nums[j] > insert_value:
				nums[j+1], nums[j] = nums[j], insert_value
			j -= 1
	return nums


sorted_Data = insert_sort(init_random_data)
print("\nsorted list:")
print(sorted_Data)