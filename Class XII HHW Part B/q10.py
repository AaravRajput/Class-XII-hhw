s = input("Enter a string: ")
sl = s.split(" ")

w = {}
wk = w.keys()
wv = w.values()

for i in sl:
	isin = False
	for j in wk:
		if i==j:
			isin = True
			break
	if isin:
		c = w[i]
		w[i] = c+1
	if not isin:
		w[i] = 1
'''
Second most frequent word....
Already have unique words and their word counts
get max count and add word
remove count
get max again and add word
'''
wc = list(wv)
ww = list(wk)
maxc = max(wc)
wc.pop(wc.index(maxc))
maxc = max(wc)
print('Second most frequent word : ',ww[wc.index(maxc)])