def check_non_negative(index):
	def validator(f):
		def wrap(*args):
			if args[index] < 0:
				raise ValueError('Argument {} must be non-negative'.format(index))
			return f(*args)
		return wrap
	return validator



@check_non_negative(1)
def create_list(value,size):
	return [value]*size

@check_non_negative(1)
def add_item(l,a):
	for i in a:
		l.append(i)
	return l



l = create_list(6,4)
l = add_item(1,[1,2,3])


