i = 0; j = 1; m = 0
while(i < len(strs)):
	while(j < len(strs)):
		cur = compare()
		if cur == 0:
			m = -1
			break
	if m == -1:
		break
	i+=1
	j = i+1
return m

compare(a,b):
	if a == b:
		return 0
	else:
		return max(len(a),len(b))
