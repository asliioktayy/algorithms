def insertion_sort(arr):
	k = 1
	while k < len(arr):
		num = arr[k]
		j = 0
		for i in range(k-1, -1, -1):
			if num < arr[i]:
				tmp = arr[i]
				arr[i] = num
				arr[k-j] = tmp
				j += 1
		k += 1
	return arr
				
arr = [1, 12, 4, 2, 8]
insertion_sort(arr)