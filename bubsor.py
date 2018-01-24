n = int(input("Enter size of array: "))
A = []
print("Enter ", n, " elements")
for i in range(n):
    A.append(int(input()))
flag = True
countloop = countswap = 0
while i in range(len(A) - 1, 0, -1) and flag is True:
    flag = False
    for j in range(i):
        if A[j] > A[j + 1]:
            flag = True
            A[j], A[j + 1] = A[j + 1], A[j]
            countswap += 1
        countloop += 1
    i += 1
print("Sorted list is", A)
print("countloop = ", countloop, "\ncountswap = ", countswap)
