def fibBottomUp(n):
	evens = []
	if n == 1 or n == 2:
		return 1
	bottom_up = [None] * (n+1)
	bottom_up[0] = 1
	bottom_up[1] = 1
	
	for i in range(2, n+1):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
		if bottom_up[i] % 2 == 0:
			evens.append(bottom_up[i])
	return sum(evens)
	

print(fibBottomUp(34))

