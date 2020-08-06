s = input("Enter comma seperated numbers ")
sl=s.split(',')
m=1
for i in sl:
	m=m*int(i)
print(m)