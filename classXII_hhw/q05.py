'''
Write a program to count the frequency of an element in a given list.
'''

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


print(lii)

x = input("Enter element to be searched ")
c=0
for i in lii:
	if i==x:
		c+=1
print("{0} occurs {1} times in the list".format(x,c))