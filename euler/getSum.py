def getSum(N):
	list = []
	for e in range(N):
		if e%3 ==0 or e%5 == 0:
			list.append(e)
	print(list)
	return sum(list)

print(getSum(1000))
