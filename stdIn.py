

def IOWrapper(func):
	def wrapper():
		fp = open(0).read()
		for line in fp.split('\n'):
			func(line)
	return wrapper

@IOWrapper
def doThing(i):
	print(i)



print(doThing())
