def numIslands(grid):
	islandNum = 0
	if grid == None:
		return 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '1':
				islandNum+=1
				print("count", islandNum)
				flip(grid,i,j)
	return islandNum
                    
                    
def flip(grid,i,j):
	if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0):
		return
	grid[i][j] = 0
	flip(grid, i+1, j)
	flip(grid, i-1, j)
	flip(grid, i, j+1)
	flip(grid, i, j-1)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(numIslands(grid))
