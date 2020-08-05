'''
Write a menu driven program in python with following opotions:
	1. Calculate the factorial of number N 
	2. Display fibbonacci sequence (0 to N)
	3. Check wether the number is armstrong or not
	4. Check wether the number is palindrome or not
	5. Display table of number N
	6. Exit
'''
def printmenu():
	print("\n\n \t1. Calculate the factorial of number N\n \
	2. Display fibbonacci sequence (0 to N)\n \
	3. Check wether the number is armstrong or not\n\
	4. Check wether the number is palindrome or not\n\
	5. Display table of number N\n\
	6. Exit\n\n\
		")

def menu():

	while True:
		usrChoice = input("Enter choice [1-6]: ")
		if usrChoice.isnumeric():
			if int(usrChoice) == 1:
				fact()
			elif int(usrChoice) == 2:
				fib()
			elif int(usrChoice) == 3:
				arm()
			elif int(usrChoice) == 4:
				pal()
			elif int(usrChoice) == 5:
				multiples()
			elif int(usrChoice) == 6:
				break
			else:
				print("\n\nENTER A NUMBER FROM 1 TO 6 \n\n")
		else:
			print("\n\nENTER A NUMBER NOT YOUR EMOTIONS \n\n")

def fact():
	N = int(input("\nEnter a number "))
	f = 1
	for i in range(f,N+1):
		f=f*i
	print("\nFactorial of {0} is {1}".format(N,f))
	printmenu()

def fib():
	s = 0
	c = 0
	n = 1
	r = int(input("\nEnter a number "))
	print("\nThe first {0} numbers of fibbonacci sequence are :".format(r))
	for i in range(r-1):
		print(c,end=" , ")
		s=c
		c=n
		n=c+s
	print(c)
	printmenu()

def arm():
	N = input("\nEnter a number ")
	summ = 0
	for i in N:
		summ += int(i)**len(N)
	if int(N) == summ:
		print("\n{0} is an Armstrong number".format(N))
	else:
		print("\n{0} is not an Armstrong number".format(N))

	printmenu()

def pal():
	N = input("\nEnter a number ")
	straight = list(N)
	reverse = []
	for i in range(len(straight)-1,-1,-1):
		reverse.append(straight[i])

	ispal=True

	for i in range(len(straight)):
		if not straight[i] == reverse[i]:
			ispal = False
			break

	if ispal:
		print("\n{0} is a pallindrome".format(N))
	else:
		print("\n{0} is not a pallindrome".format(N))

	printmenu()

def multiples():
	N = int(input("\nEnter a number "))
	print("\n Table of {0} :".format(N))
	for i in range(1,11):
		print("{0} x {1} = {2}".format(N,i,N*i))
	printmenu()

printmenu()
menu()