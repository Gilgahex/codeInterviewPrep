
sums = pow(sum(range(1,101)),2)

def square(n):
	return pow(n,2)

powers = sum(list(map(square, range(1, 101))))

print(sums-powers)
