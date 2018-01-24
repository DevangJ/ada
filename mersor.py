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
    # A = list(range(len(left)+len(right)))
    # i = j = k = 0
    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         A[k] = left[i]
    #         i += 1
    #     else:
    #         A[k] = right[j]
    #         j += 1
    #     k += 1
    # while i < len(left):
    #     A[k] = left[i]
    #     i += 1
    #     k += 1
    # while j < len(right):
    #     A[k] = right[j]
    #     j += 1
    #     k += 1
    # return A


def mergesort(A):
    if(len(A) < 2):
        return A
    return merge(mergesort(A[:len(A) >> 1]), mergesort(A[len(A) >> 1:]))
    # left = []
    # right = []
    #mid = len(A) >> 1
    # for i in range(mid):
    #     left.append(A[i])
    # for i in range(mid, len(A)):
    #     right.append(A[i])
    # mergesort(left)
    # mergesort(right)
    # merge(left, right, A)


A = []
n = int(input("Enter array size: "))
print("Enter ", n, " elements")
for i in range(n):
        A.append(int(input()))
A = mergesort(A)
print(A)
