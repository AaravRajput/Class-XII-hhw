d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}

d3={}

for i in list(d2.keys()):
	isin = False
	for j in list(d3.keys()):
		if i==j:
			isin=True
	if not isin:
		d3[i]=d2[i]
	else:
		d3[i]=d3[i]+d2[i]

for i in list(d1.keys()):
	isin = False
	for j in list(d3.keys()):
		if i==j:
			isin=True
	if not isin:
		d3[i]=d1[i]
	else:
		d3[i]=d3[i]+d1[i]

print(d3)