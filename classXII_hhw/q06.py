li = [3,25,13,6,35,8,14,45]
newLi = []

index=0
for i in li:
	if i%5==0:
		newLi.insert(index-1,i)
		index+=1
		continue
	else:
		newLi.append(i)
	index+=1

print(li)
print(newLi)
