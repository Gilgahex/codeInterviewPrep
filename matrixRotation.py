#Given a square matrix (A) test if and square matrix input (T) is a rotation of it

def rotation(A,T):
	if len(T[0]) == len(A[0]) and len(T) == len(A):
		size = len(A[0])-1
		c = 0
		for rot in range(4):
			while size-i>0:
				A[i][j] = A[j][size-c]
				c+=1
			print("completed rotation",A)
		if A == T:
			return True
		return False
	else:
		return False



A = [[1,2,3],[4,5,6],[7,8,9]]
T = [[7,4,1],[8,5,2],[9,6,3]]
print(rotation(A,T))
