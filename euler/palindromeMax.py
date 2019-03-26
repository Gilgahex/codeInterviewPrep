
def palindromes(n):
	vals = []
	for i in range(91,n+1):
		for j in range(99,n+1):
			s = str(i*j)
			if s[::-1] == s:
				vals.append((i,j,s))
	print(vals)
	#return max(vals)
	
print(palindromes(999))
