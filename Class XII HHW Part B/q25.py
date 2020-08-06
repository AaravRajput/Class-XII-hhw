d = {}
count = 0
while True:
	choice = input("Enter list[comma-separated] or q to break ")
	if choice == 'q':
		break
	else:
		ch = list(choice.split(','))
		d[count]=ch
		count += 1

dk=list(d.keys())

for k in dk:
	li = d[k]
	c = 0
	for j in li:
		c+=1
	print("No. of elements in list {0} is {1}".format(k,c))
