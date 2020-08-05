
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

newLi=[]

for i in range(0,len(lii)):
	newLi.insert(i,lii[i-1])

print(li)
print(lii)
print(newLi)