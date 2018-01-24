def binser(A, low, high, key):
    if low > high:
        return False
    global countloop
    countloop += 1
    mid = (low + high) >> 1
    return mid if A[mid] is key else binser(A, low, mid - 1, key) if A[mid] > key else binser(A, mid + 1, high, key)


n = int(input("Enter size of array: "))
A = []
countloop = 0
print("Enter ", n, " elements")
for i in range(n):
    A.append(int(input()))
key = int(input("Enter key: "))
result = binser(A, 0, n-1, key)
if result is False:
    print("Element not found")
else:
    print("Element present at index = ", result)
print("countloop = ", countloop)
