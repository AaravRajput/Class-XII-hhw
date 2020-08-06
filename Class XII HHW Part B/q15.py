l =[]
for i in range(1,30):
	l.append(i**2)
x=[]

for i in l[0:5]:
	x.append(i)
for i in l[-5:]:
	x.append(i)

print(x)