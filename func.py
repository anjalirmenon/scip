def f(n):
	if n < 3:
		return n
	else:
		return f(n-1) + 2 * f(n-2) + 3 * f(n-3)
