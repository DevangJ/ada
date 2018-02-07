def partition(A, low, high):
	i = low - 1
	pivot = A[high]
	for j in range(low, high):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[high] = A[high], A[i + 1]
	return i + 1


def quicksort(A, low, high):
	if low < high:
		pi = partition(A, low, high)
		quicksort(A, low, pi - 1)
		quicksort(A, pi + 1, high)


n = int(input("Enter array size: "))
A = []
print("Enter", n, "elements")
for i in range(n):
	A.append(int(input()))
quicksort(A, 0, n - 1)
print("Sorted array is", A)
