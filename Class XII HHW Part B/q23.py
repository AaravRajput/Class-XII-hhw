d={}
while True:
	choice = input("Enter key,value pairs [comma-separated] or q to break : ")

	if choice.lower() == 'q':
		break
	else:
		ch = list(choice.split(','))
		d[ch[0]]=ch[1]

dv = list(d.values())
dv.sort()

print("Highest 3 values : ")
for i in range(1,4):
	print(dv[-i])