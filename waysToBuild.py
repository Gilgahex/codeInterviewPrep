
def ways(n):
	t = [0]*(n+1)
	#Base cases
	t[1] = 1; t[2] = 2; t[3]=3; 
	for i in range(4,n+1):
		t[i] = t[i-1]+t[i-2]+t[i-3]
	t = t[1:]
	return t

n = 10
r = range(1,n+1)
res = list(zip(r,ways(n)))
print(res)
