def partition(A, low, high):
	i = low - 1
	pivot = A[high]
	global swaps
	for j in range(low, high):
		swaps += 1
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[high] = A[high], A[i + 1]
	return i + 1


def quicksort(A, low, high):
	global countloop
	if low < high:
		pi = partition(A, low, high)
		countloop += 1
		quicksort(A, low, pi - 1)
		countloop += 1
		quicksort(A, pi + 1, high)


n = int(input("Enter array size: "))
A = []
countloop = 0
swaps = 0
print("Enter", n, "elements")
for i in range(n):
	A.append(int(input()))
countloop += 1
quicksort(A, 0, n - 1)
print("Sorted array is", A)
print("Number of function calls =", countloop)
print("Number of comparisons =", swaps)
