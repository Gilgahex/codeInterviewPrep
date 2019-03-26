def compare(S,T):
	def build(S):
		ans = []
		for c in S:
			if c!="#":
				ans.append(c)
			elif ans:
				ans.pop()
		return "".join(ans)
	return build(S)==build(T)
	
S="#a#c"
T="c"

print(compare(S,T))
			
			
