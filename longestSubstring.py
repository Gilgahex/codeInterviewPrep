def longestSubstring(s):
	maxLen = i = j = 0
	hashSet = set()
	while (j < len(s)):
		if s[i] not in hashSet:
			hashSet.add(s[i])
			j+=1
			maxLen = max(maxLen, j-i)
		else:
			hashSet.remove(s[i])
			i+=1
	return maxLen
			
		

s = "abcabcbb"
print(longestSubstring(s))
