l1 = input("Enter comma seperated values ").split(',')
l2 = input("Enter comma seperated values ").split(',')
print('''
	Before Appending
	L1 is {0}
	L2 is {1}
	'''.format(l1,l2))
for i in l2:
	l1.append(i)
print('''
	After Appending
	L1 is {0}
	L2 is {1}
	'''.format(l1,l2))