#import time
def towerOfHanoi(n, from_peg, to_peg, aux_peg):
	global countloop
	if n is 1:
		print("Move Disk 1 from", from_peg, "to", to_peg)
		return
	countloop += 1
	towerOfHanoi(n-1, from_peg, aux_peg, to_peg)
	print("Move Disk", n, "from", from_peg, "to", to_peg)
	countloop += 1
	towerOfHanoi(n-1, aux_peg, to_peg, from_peg)


countloop = 0
n = int(input("Enter number of disks\n"))
countloop += 1
#x = time.time()
towerOfHanoi(n, 'A', 'C', 'B')
#y = time.time()
print("Number of function calls =", countloop)
y -= x
print(y)
