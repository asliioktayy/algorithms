def binary_search(arr, l, r, x):
	mid = (l + r) / 2
	while r >= l:
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			r = mid - 1
			mid = (l + r) / 2
		else:
			l = mid + 1
			mid = (l + r) / 2
	return -1

arr = [1,5,34,67,99]
result = binary_search(arr, 0, len(arr) - 1, 10)
if result == -1:
	print 'not found'
else:
	print result