from sum_term import *
def inc(x):
	return x + 1
def cube(x):
	return x * x * x
def sum_cube(a, b):
	return sum(cube, a, inc, b)
