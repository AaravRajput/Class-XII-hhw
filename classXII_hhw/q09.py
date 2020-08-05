summ=0
while True:
	e = input("Enter a number or type \'Done\' : ")
	if e.isnumeric():
		summ+=int(e)
	else:
		if e.upper()=='DONE':
			break
		else:
			print("You need to enter a number")

print(summ)