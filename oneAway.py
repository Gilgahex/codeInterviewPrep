#This function tests whether two strings are only one char different as defined by
#1) Same length, but one char out of place 
#2) s1 missing one char from s2
#3) s2 missing one char from s1

def oneAway(s1,s2):
	count = 0
	#True if and only if one char diff
	if len(s1) == len(s2):
		for e in range(len(s1)):
			if s1[e] != s2[e]:
				count+=1
		if count == 1:
			return True
		else:
			return False
	#If one char missing from each other
	#Use slicing to jump over nth char
	if len(s2) == len(s1) + 1:
		for e in range(len(s2)):
			if s2[:e]+s2[(e+1):] == s1:
				return True
	if len(s1) == len(s2) + 1:
		for e in range(len(s1)):
			if s1[:e]+s1[(e+1):] == s2:
				return True
	else:
		return False

#Test cases
#One char diff
s1="abcde"
s2="abfde"

#First string missing char
s3="xyz"
s4="xyaz"

#Second string missing char
s5=s1
s6="abde"


print(oneAway(s1,s2))
print(oneAway(s3,s4))
print(oneAway(s5,s6))
print(oneAway(s3,s6))
