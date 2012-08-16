def sumint(a,b):
	if a > b:
		return 0
	else:
		return a + sumint(a+1, b)
