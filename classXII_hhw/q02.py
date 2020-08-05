'''
Write a menu driven program in python with following opotions:
	1. Check wether string is pallindrome or not
	2. Calculate total characters of string
	3. Calculate total vowels in string
	4. Calculate total spaces in string
	5. Display string in reverse order
	6. Exit
'''
def printmenu():
	print("\n\n \t1. Check wether string is pallindrome or not\n\
	2. Calculate total characters of string\n\
	3. Calculate total vowels in string\n\
	4. Calculate total spaces in string\n\
	5. Display string in reverse order\n\
	6. Exit\n\n\
		")

def menu():

	while True:
		usrChoice = input("Enter choice [1-6]: ")
		if usrChoice.isnumeric():
			if int(usrChoice) == 1:
				pal()
			elif int(usrChoice) == 2:
				totC()
			elif int(usrChoice) == 3:
				vowC()
			elif int(usrChoice) == 4:
				spaC()
			elif int(usrChoice) == 5:
				reverse()
			elif int(usrChoice) == 6:
				break
			else:
				print("\n\nENTER A NUMBER FROM 1 TO 6 \n\n")
		else:
			print("\n\nENTER A NUMBER NOT YOUR EMOTIONS \n\n")

def pal():
	inp = input("\nEnter a string ")
	N = list(inp)
	reverse = []
	for i in range(len(N)-1,-1,-1):
		reverse.append(N[i])

	ispal=True

	for i in range(len(N)):
		if not N[i] == reverse[i]:
			ispal = False
			break

	if ispal:
		print("\n{0} is a pallindrome".format(inp))
	else:
		print("\n{0} is not a pallindrome".format(inp))

	printmenu()

def reverse():
	inp = input("\nEnter a string ")
	N = list(inp)
	reverse = []
	for i in range(len(N)-1,-1,-1):
		reverse.append(N[i])
	revStr =''
	for i in reverse:
		revStr+=i
	print("\nThe reverse of {0} is {1}".format(inp,revStr))

	printmenu()

def totC():
	inp = input("\nEnter a string ")
	print("\nTotal number of characters in {0} is {1}".format(inp,len(inp)))
	printmenu()

def vowC():
	inp = input("\nEnter a string ")
	N = list(inp)
	vowels = ['a','e','i','o','u']
	hasVow=False
	vowIS =[]
	vowAt=[]
	c = 0
	ind = 0
	for i in N:
		for j in vowels:
			if i.upper()==j.upper():
				c+=1
				hasVow=True
				vowIS.append(i)
				vowAt.append(ind)
		ind+=1

	if hasVow:
		print("\n{0} has {3} vowels {1} at indices {2} ".format(inp, vowIS, vowAt,c))
	else:
		print("\n{0} has no vowels".format(inp))

	printmenu()

def spaC():
	inp = input("\nEnter a string ")
	hasSpace = False
	c=0
	ind=0
	spaceAt=[]
	for i in inp:
		if i==" ":
			c+=1
			hasSpace = True
			spaceAt.append(ind)
		ind+=1

	if hasSpace:
		print("\n{0} has {1} spaces at indices {2} ".format(inp,c,spaceAt))
	else:
		print("\n{0} has no spaces ".format(inp))

	printmenu()

printmenu()
menu()