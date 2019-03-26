import math

def is_pythagorean_triple(a,b,c):
	return a**2+b**2==c**2

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if c < b:
            break
        if is_pythagorean_triple(a, b, c):
            print(a, b, c)
            print("Product: {}".format(a * b * c))
            exit(0)
	
