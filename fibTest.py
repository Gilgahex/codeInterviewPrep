def fibMemo(n, memo):
	if memo[n] != None:
		return memo[n]
	if n == 1 or n == 2:
		result = 1
	else:
		result = fib(n-1) + fib(n-2)
	memo[n] = result
	return result
	
def fib(n):
	if n == 1 or n == 2:
		result = 1
	else:
		result = fib(n-1) + fib(n-2)
	return result


def fibBottomUp(n):
	if n == 1 or n == 2:
		return 1
	bottom_up = [None] * (n+1)
	bottom_up[0] = 1
	bottom_up[1] = 1
	
	for i in range(2, n+1):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	return bottom_up[n]
	
print(fibBottomUp(50))
