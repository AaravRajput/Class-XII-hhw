s = input("Enter a string")
sl = s.split()
fs=''

for i in s:
	isin=False
	for j in fs:
		if i==j:
			isin=True
			break
	if not isin:
		fs+=i

print(fs)

