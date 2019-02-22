def findPair(lst,target):
	memo = []
	res = []
	for i in range(len(lst)):
		if target-lst[i] in memo:
			res.append((lst[i], target-lst[i]))
		memo.append(lst[i])
	return res

lst = [1,3,6,5,5,7,4,9]
res = findPair(lst,10)
print(res)
			
