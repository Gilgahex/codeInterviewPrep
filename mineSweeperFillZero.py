import queue
import numpy as np

def click(field, row_n, col_n, click_i, click_j):
	to_check = queue.Queue()
	if field[click_i][click_j] == 0:
		field[click_i][click_j] = -2
		to_check.put((click_i,click_j))
	else:
		return field
	
	while to_check.empty() == False:
		(current_i,current_j) = to_check.get()
		for i in range(current_i+1,current_i+2):
			for j in range(current_j-1, current_j+2):
				if(0<= i < row_n and 0 <=j < col_n and field[i][j] == 0):
					field[i][j] = -2; to_check.put((i,j))
	return field


field = [[-1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,-1]]
postClick = click(field, 4,4,0,2)
print( np.matrix(postClick) )
