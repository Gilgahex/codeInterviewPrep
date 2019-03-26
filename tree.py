class Node(object):	
	def __init__(self,data):
		self.data = data
		self.l = []
		self.r = []
		self.children = []
	
	def __init__(self,data,l,r):
		self.data = data
		self.l = l
		self.r = r
		self.children = [l,r]
		
	
	def getNumChildren(self):
		return len(children)
		
	def getChild(self,n):
		return children[n]
	
	def add_child(self,obj):
		self.children.append(obj)
	
	def add_L(self,obj):
		self.l.append(obj)
	
	def add_R(self,obj):
		self.r.append(obj)
	
	
	
root = Node(1)
p = Node(2)
q = Node(3)

root.add_L(p)
root.add_R(q)
for i in 


root = Node(0,1,2)
for i in root.children:
	print(i)
