sl = input("Enter comma seperated values: ").split(',')
w = []
for i in sl:
	isin = False
	for j in w:
		if i==j:
			isin = True
			break
	if not isin:
		w.append(i)

print(w)
