def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])
    
   
m = [[1,2,3],[4,5,6],[7,8,9]]

#print([*zip(*m)][::-1])
#print(*m.pop())
print(spiralOrder(m))
