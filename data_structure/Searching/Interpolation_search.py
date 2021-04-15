




arr = [2, 3, 4, 10, 40]

def interpolation_search(arr, target):
	lower = 0
	upper = len(arr) - 1
	while lower <= upper:
		mid = ( (upper-lower) * (target-arr[lower]) / (arr[upper]-arr[lower]) + lower )
		if mid < lower or mid > upper: break
		
		if target < arr[mid]:
			upper = mid - 1
		elif target > arr[mid]:
			lower = mid + 1
		else:
			return mid
	return -1


result = interpolation_search(arr, 4)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")