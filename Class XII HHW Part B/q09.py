s = input("Enter string ")
sl=[]
for i in s:
	sl.append(i)
summ=int()
for i in sl:
	if i.isnumeric():
		summ=summ+int(i)
print(summ)