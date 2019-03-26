def whatever(l):
	count = subcount = 0
	for e in l:
		if e == 0:
			subcount+=1
		if e == 1:
			count = max(count,subcount)
			subcount = 0
	if subcount == 0:
		if count%2 ==0:
			return count-2
		else:
			return count-1
	else:
		return count

print(whatever([1,0,0,1]))
