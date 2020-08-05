classes = {}

def printmenu():
	print('''\n\n
		------------------------
		|1. Add Record         |	
		------------------------
		|2. View Record        |
		------------------------
		|3. Exit               |
		------------------------
		\n\n''')


def menu():
	while True:
		choice = input("Enter your choice : ")
		if choice.isnumeric():
			if int(choice)==1:
				addrec()
			elif int(choice)==2:
				viewrec()
			elif int(choice)==3:
				break
			else:
				print("Enter 1, 2 or 3... How hard can that be...")
		else:
			print("Enter a NUMBER maybe ?¿")

def addrec():
	cl = int(input("\nEnter class "))
	name = input("\nEnter class teacher's full name ")
	classes[cl]=(name)

	printmenu()

def viewrec():
	query=int(input("\nEnter class "))
	isin = False
	for i in classes.keys():
		if i==query:
			isin = True
			break

	if isin:
		print("\n\nClass :{0}\nClass teacher :{1}".format(query,classes[query]))
	else:
		print("Class not found")

	printmenu()


printmenu()
menu()