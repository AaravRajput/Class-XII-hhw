def capc(li):
	newString = ""
	for i in li:
		newString += i[0].upper()
		newString += i[1:-1]
		newString += i[-1].upper()
		newString += " "

	print(newString)


li = input("Enter comma seperated values : ")
c =''
lii = []

for i in li:
	if not i==',':
		c += i
	if i==',':
		lii.append(c)
		c=''
lii.append(c)

capc(lii)