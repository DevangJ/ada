n = int(input("Enter size of array: "))
A = []

print("Enter ", n, " elements")

for i in range(n):
    A.append(int(input()))

for i in range(len(A)):
    A[i + A[i:].index(min(A[i:]))], A[i] = A[i], A[i + A[i:].index(min(A[i:]))]
    countloop += 1

# countloop = countswap = 0
#
# for i in range(len(A)):
#     m = i
#     for j in range(i + 1, len(A)):
#         if A[m] > A[j]:
#             m = j
#         countloop += 1
#     if i is not m:
#         A[i], A[m] = A[m], A[i]
#         countswap +=1

print("Sorted list is", A)
print("countloop = ", countloop)
