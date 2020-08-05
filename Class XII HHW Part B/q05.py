student_records = {}

def printmenu():
	print('''\n\n
		------------------------
		| Student Management   |
		------------------------
		|1. Add Record         |	
		------------------------
		|2. View Record        |
		------------------------
		|3. Delete Record      |
		------------------------
		|4. Exit               |
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
				delrec()
			elif int(choice)==4:
				break
			else:
				print("Enter 1, 2,3 or 4... How hard can that be...")
		else:
			print("Enter a NUMBER maybe ?¿")

def addrec():
	name = input("\nEnter student's full name ")
	sub = int(input("\nEnter number of subjects taken "))
	subjects={}
	for i in range(sub):
		s=input("\nEnter subject ")
		m=input("\nEnter percentage in {0} ".format(s))
		subjects[s]=m
	student_records[name]=(subjects)

	printmenu()

def viewrec():
	k=list(student_records.keys())
	v=list(student_records.values())
	for i in range(len(k)):
		print(k[i])
		w=list(v[i].keys())
		u=list(v[i].values())
		for j in range(len(w)):
			print(w[j]+" : "+u[j])

	printmenu()

def delrec():
	query=input("\nEnter name of student ")
	isin = False
	for i in student_records.keys():
		if i==query:
			isin = True
			break

	if isin:
		student_records.pop(query)
		viewrec()
	else:
		print("Student not found")



printmenu()
menu()