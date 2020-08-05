tup1 = ()
n = int(input("Enter number of elements of tuple : "))
for i in range(n):
	e = int(input("Enter a number "))
	tup1 = tup1+(e,)

for i in tup1:
	print(i)

print("Minimum is {1}\nMaximum is {0}".format(max(tup1),min(tup1)))