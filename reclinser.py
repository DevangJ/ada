def linser(A, n, key, countcall):
    if n == -1:
        print("countcall = ", countcall)
        return False
    elif A[len(A) - n] == key:
        print("countcall = ", countcall)
        return len(A) - n
    return linser(A, n - 1, key, countcall + 1)


n = int(input("Enter size of array: "))
A = []

print("Enter ", n, " elements")

for i in range(n):
    A.append(int(input()))

key = int(input("Enter key: "))
result = linser(A, n, key, 0)

if result is False:
    print("Element not found")
else:
    print("Element present at index = ", result)
