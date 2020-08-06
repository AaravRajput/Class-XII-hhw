s = input("Enter string: ")
sl = s.split(' ')
fs = ''
w=''
for i in sl:
	if not len(i)==1:
		w+=i[0].upper()+i[1:-1]+i[-1].upper()
		fs+=w+' '
		w=''
	else:
		fs+=i.upper()+' '

print(fs)