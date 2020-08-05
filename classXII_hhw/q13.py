def primeCheck(N):
	isPrime = True
	for i in range(2,N):
		if N%i==0:
			isPrime = False
	return isPrime

e = int(input("Enter a digit "))

if primeCheck(e):
	print("Number is prime")
else:
	print("Number is not prime")