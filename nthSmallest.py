import heapq

def maxSum(lst):
	lst = sorted(lst)
	return (lst[-2]+lst[-1])

def nthSmallestHeap(lst,n):
	res = heapq.nsmallest(n,lst)
	print(res)
	return res[-1]

def nthLargestHeap(lst,n):
	return heapq.nlargest(n,lst)[-1]

def maxSumHeap(lst):
	return sum(heapq.nlargest(2,lst))
	
def nthSmallestPivot(data,n):
	
	while(True):
		swap = random.randrange(len(data))
		data[0], data[swap] = data[swap], data[0]
		it = iter(data)
		pivot, piviotcount = it.next(), 1
		under, over = [], []
		ua, oa = under.append, over.append
		for elem in it:
			r = cmp(elem, pivot)
		if r
	

lst = [-15,-40,-80,-2,-1,0,1,2,3,100,4,7]

print(nthSmallestPivot())
	
