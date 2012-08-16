def large_square_sum(a,b,c):
	list = []
	list.append(a)
	list.append(b)
	list.append(c)
	list.sort()
	s = list[1]
	t = list[2]
	j = s * s + t * t
	print j
