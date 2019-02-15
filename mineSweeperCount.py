def gridCount(bombs, row_n, col_n):
	field = [[0] * row_n for i in range(col_n)]
	for bomb in bombs:
		row_i = bomb[0]; col_i = bomb[1]
		field[row_i][col_i] = -1
		#Loop over 9 elements around each bomb
		#Since python3 range (start,end) is not inclusive on end, add an extra one
		#for i from row_-1 to row_1+2 == range(row_i,row_i+2); Same for cols
		for i in range(row_i-1,row_i+2):
			for j in range(col_i-1,col_i+2):
				if (0<=i<row_n and 0<=j<col_n and field[i][j]!=-1):
					field[i][j]+=1
	return field
	

print(gridCount([[0,0],[0,1]],3,3))
