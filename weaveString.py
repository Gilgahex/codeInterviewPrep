
def weave(s1,s2):
	s = ""
	maxLen = max(len(s1),len(s2))
	for i in range(maxLen):
		try:
			s+=s1[i]
			s+=s2[i]
		except IndexError:
			s+=""
	return s

s1 = "ti sahde esg."
s2 = "hsi  idnmsae"

print(weave(s1,s2))
