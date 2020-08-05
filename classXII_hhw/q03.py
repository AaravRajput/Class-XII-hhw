'''
Write a program to calculate income tax of an employee on the basis of basic salary and total
savings inputted by the user as per the given slabs: -
	*No tax for individual with income less than Rs.2.5 lakhs
	*0% to 5% tax with income Rs.2.5 lakhs to Rs.5 lakhs
	*20% tax with income Rs.5 lakhs to Rs.10 lakhs
	*Investments up to Rs.1.5 lakhs under Sec 80 C can save up to Rs.45000 in taxes
'''

sal = int(input("Enter salary (Annual) "))
if sal <= 250000:
	print("No tax to be paid")
elif sal <= 500000:
	sav = int(input("Enter investments "))
	if sav >= 150000:
		print("Tax to be paid = {0}".format((sal*5/100)-45000))
	else:
		print("Tax to be paid = {0}".format(sal*5/100))
elif sal <= 1000000:
	sav = int(input("Enter investments "))
	if sav>=150000:
		print("Tax to be paid = {0}".format((sal*20/100)-45000))
	else:
		print("Tax to be paid = {0}".format(sal*20/100))
