n = int(input("Enter size of array: "))
A = []

print("Enter ", n, " elements")

for i in range(n):
    A.append(int(input()))

key = int(input("Enter key: "))
result = False
countloop = 0

for i in range(n):
    if A[i] == key:
        result = i
        break
    countloop += 1

if result is False:
    print("Element not found")
else:
    print("Element present at index = ", result)

print("countloop = ", countloop)
