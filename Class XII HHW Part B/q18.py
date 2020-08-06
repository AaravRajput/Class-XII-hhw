d1 = {'A':1,'B':2,'C':3}
d2={'D':4}

d3={}

for i in list(d1.keys()):
	d3[i]=d1[i]
for j in list(d2.keys()):
	d3[j]=d2[j]

print(d3)