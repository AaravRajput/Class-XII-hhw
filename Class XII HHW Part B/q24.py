d = {}
count = 0
while True:
	choice = input("Enter list[comma-separated] or q to break")
	if choice == 'q':
		break
	else:
		ch = list(choice.split(','))
		d[count]=ch
		count += 1

print(d)
sorted_d = {}
for k,v in d.items():
	sorted_d[k] = sorted(v)

print(sorted_d)