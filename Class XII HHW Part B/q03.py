tup1 = ()
n = int(input("Enter number of elements of tuple : "))
for i in range(n):
	e = int(input("Enter a number "))
	tup1 = tup1+(e,)

tup2 = ()
m = int(input("Enter number of elements of tuple : "))
for j in range(m):
	f = int(input("Enter a number "))
	tup2 = tup2+(f,)

print("BEFORE SWAPPING")
print("\nFirst tuple: {0}".format(tup1))
print("\nSecond tuple: {0}".format(tup2))

tup1, tup2 = tup2, tup1

print("AFTER SWAPPING")
print("\nFirst tuple: {0}".format(tup1))
print("\nSecond tuple: {0}".format(tup2))
