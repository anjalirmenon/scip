def inc (x):
	return x+1
def dec (x):
	return x-1
def new_add(a, b):
	if a == 0:
		return b
	else:
		return dec(a) + inc(b)
