d = input("Enter date in format MMDDYYYY : ")
m = d[0:2]
date = d[2:4]
y = d[4:]

months = ('January','February','March','April','May','June','July','August','September','October','November','December')

month = months[int(m)-1]

print("The date enterred is {0} {1}, {2} ".format(month,date,y))