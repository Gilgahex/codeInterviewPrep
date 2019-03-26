def licenseKeyFormatting(S, K):
	S = "".join(c.upper() for c in S if c != '-')
	
	S = [
		S[max(i - K, 0):i] for i in range(len(S), 0, -K) [::-1]
		]
	return "-".join(S)
	
testString = "2-5g-3-J"
print(licenseKeyFormatting(testString,2))
