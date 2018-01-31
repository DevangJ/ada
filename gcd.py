def gcd(a, b):
	global countloop
	if b is 0:
		return a
	countloop += 1
	return gcd(b, a % b)

countloop = 0
print("Enter 2 numbers")
a = int(input("1. "))
b = int(input("2. "))
countloop += 1
print("GCD of ", a, " and ", b, " is ", gcd(a, b))
print("Number of function calls =", countloop)
