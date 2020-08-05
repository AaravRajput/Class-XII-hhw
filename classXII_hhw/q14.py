li = input("Enter hyphen seperated values : ")
c =''
lii = []

for i in li:
	if not i=='-':
		c += i
	if i=='-':
		lii.append(c)
		c=''
lii.append(c)

lii.sort()

for i in lii:
	print(i,end="-")