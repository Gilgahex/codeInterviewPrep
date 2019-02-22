#Bottom up determination of the minimum number of steps from n->1
#With the operations /3, /2, -1

def nToOne(n):
	tab = [-1]*(n+1); tab[0] = tab[1] = 0; tab[2] = 1
	if n == 0:
		return "Invalid"
	if n == 1:
		return 0
	for i in range(2,n+1):
		#Recast to int as a/b casts a&b to floats automatically
		if i%2 == 0:
			tab[i] = min( tab[int(i/2)]+1, tab[i-1]+1 )
		if i%3 == 0:
			tab[i] = min( tab[int(i/3)]+1, tab[i-1]+1 )
		else:
			tab[i] = tab[i-1]+1
	#Drop Base Cases so zip will not need +2 offset Later
	tab = tab[2:]
	return tab

n = 20
r = range(2,n+1)
tab = nToOne(n)
pairs = list(zip(r,tab))
print(pairs)
