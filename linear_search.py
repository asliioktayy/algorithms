def linear_search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1

arr = [15, 3, 4, 12]
linear_search(arr, 4)
