def anagram(s1,s2):
	s1 = sorted(s1.lower().replace(" ",""))
	s2 = sorted(s2.lower().replace(" ",""))
	if s1 == s2:
		return True
		
	else:
		return False
		
s1 = "Clint Eastwood"
s2 = "Old West Action"
print(anagram(s1,s2))
