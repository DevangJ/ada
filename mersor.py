def merge(left, right):
    A = []
    i = j = 0
    global countloop
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A.append(left[i])
            i += 1
        else:
            A.append(right[j])
            j += 1
        countloop += 1
    A.extend(left[i:])
    A.extend(right[j:])
    return A


def mergesort(A):
    if(len(A) < 2):
        return A
    return merge(mergesort(A[:len(A) >> 1]), mergesort(A[len(A) >> 1:]))


A = []
n = int(input("Enter array size: "))
countloop = 0
print("Enter ", n, " elements")
for i in range(n):
        A.append(int(input()))
A = mergesort(A)
print(A)
print("countloop = ", countloop)
