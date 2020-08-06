d1 = {}
d2 = {}

print('Input D1')
while True:
	e = list(input("\nEnter a key value pair [comma-seperated] or q to continue ").split(','))
	if e==['q']:
		break
	else:
		d1[e[0]]=e[1]

print('Input D2')
while True:
	e = list(input("\nEnter a key value pair [comma-seperated] or q to continue ").split(','))
	if e==["q"]:
		break
	else:
		d2[e[0]]=e[1]

d3={}

for i in list(d1.keys()):
	d3[i]=d1[i]
for j in list(d2.keys()):
	d3[j]=d2[j]

while True:
	e=input("Enter key to search or q to quit ")
	if e=='q':
		break
	else:
		try:
			print(e+":"+d3[e])
		except:
			print("Key not found")
