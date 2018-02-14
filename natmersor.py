def merge(left, right):
	A = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			A.append(left[i])
			i += 1
		else:
			A.append(right[j])
			j += 1
	A.extend(left[i:])
	A.extend(right[j:])
	return A


def mergesort(A):
	if len(A) < 2:
		return A
	i = 0
	for i in range(1, len(A)):
		if(A[i - 1] > A[i]):
			break
	return merge(A[:i], mergesort(A[i:]))


A = []
n = int(input("Enter array size: "))
print("Enter ", n, " elements")
for i in range(n):
	A. append(int(input()))
A = mergesort(A)
print("Sorted array = ", A)
