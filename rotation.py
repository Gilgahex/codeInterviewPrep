def isRotation(A,B):
	if len(A) != len(B):
		return False
	key_A = A[0]; key_B = -1
	
	for i in range(len(A)):
		if B[i] == key_A:
			key_B = i
			break
	if key_B == -1:
		return False
	
	for i in range(len(A)):
		if A[i] != B[(i+key_B)%len(A)]:
			return False
	return True

a = [1,2,3,4,5,6,7]
b = [3,4,5,8,7,1,2]
print(isRotation(a,b))
