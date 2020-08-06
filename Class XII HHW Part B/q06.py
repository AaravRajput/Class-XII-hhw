n = int(input("Enter nymber of customers: "))

cust = {}
for i in range(n):
	name = input("Enter name : ")
	number = input("Enter phone number : ")
	item_no = int(input("\nEnter number of items bought : "))
	it_d={}
	for j in range(item_no):
		item = input("\nEnter item bought ")
		cost = input("Enter cost of {0} ".format(item))
		it_d[item]=cost
	cust[i] = (name,number,it_d)

k=list(cust.keys())
v=list(cust.values())
print('''
	╔══════════════════════╦═════════════════════════╦════════════════════════════════════════════════╦═══════════════════════════╗
	║Name                  ║Phone Number             ║Items                                           ║Cost                       ║
	╠══════════════════════╬═════════════════════════╬════════════════════════════════════════════════╬═══════════════════════════╣
	''')
for i in range(len(k)):
	n = v[i][0]
	p = v[i][1]
	w=list(v[i][2].keys())
	u=list(v[i][2].values())
	iter_items =''
	iter_costs =''
	for j in range(len(w)):
		iter_items+=(str(w[j])+',')
		iter_costs+=(str(u[j])+',')
	print('''
	║{0}                {4}║{1}                    {5}║{2}                                        {6}║{3}                       {7}║
	╠══════════════════════╬══════════════════════════╬══════════════════════════════════════════════╬═════════════════════════════╣
	'''.format(n,p,iter_items,iter_costs,('\b'*len(n)),('\b'*len(p)),('\b'*len(iter_items)),('\b'*len(iter_costs))))
