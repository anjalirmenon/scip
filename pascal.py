def pascal(row,col):
	if row == col or col == 1:
		return 1
	else:
		return pascal(row-1,col-1) + pascal(row-1, col)
