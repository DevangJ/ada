n = int(input("Enter number of vertices\n"))
A = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
	for j in range(n):
		A[i][j] = int(input())
countloop = 0
result = True
for i in range(n):
	for j in range(n):
		countloop += 1 
		if i is j:
			countloop += 1
			if A[i][j] is not 0:
				result = False
				break
		else:
			countloop += 1
			if A[i][j] is not 1:
				result = False
				break
if result is False:
	print("Not complete")
else:
	print("Complete")
print("Number of comparisons =", countloop)	
