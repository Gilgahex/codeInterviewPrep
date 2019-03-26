from Queue import PriorityQueue

class State(object):
	def __init__(self, value, parent, start = 0, goal = 0):
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0
		if parent:
			#Copies list [:]
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal
			self.solver = solver
		
	def GetDist(self):
		pass
	
	def CreateChildren(self):
		pass
		
class State_String(State):
	def __init__(self, value,parent,start =0, goal = 0):
		super(State_String, self).__init__(value,parent,start,goal)
		self.dist = self.GetDist()
	
	def GetDist(self):
		if self.value == self.goal:
			return 0
		dist = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist == abs(i - self.value.index(letter))
		return dist
	
	def CreateChildren(self):
		if not self.children:
			for i in range(len(self.goal)-1):
				val = self.value
				val = val[:i]+val[i+1]+val[i]+val[i+2:]
				children = State_String(val, self)
				selfchildren.append(child)
	
class AStar_Solver:
	def __init__(self, start, goal):
		self.path = []
		self.visitedQueue = []
		self.priorityQueue = PriorityQueue()
		self.start = start
		self.goal = goal
		
	def Solve(self):
		startState = State_string(self.start,0,self.start, self.goal)
		count = 0
		self.priorityQueue.put((0,count, startState))
		while(not self.path and self.priorityQueue.qsize):
			closestChild = self.priorityQueue.get()[2]
			closestchild.CreateChildren()
			self.visitedQeueu.append(closestchild.value)
			for child in closestchild.children:
					if child.value not in self.visitedQueue:
							count +=1
							if not child.dist:
									self.path = child.path_exists
									break
								self.priorityQueue.put((child.dist,count,child))
		if not self.path:
				print("Goal of " + self.goal + "is not possible")
		return self.path
								

##MAIN

if __name == "":
	string = ""
	goal = ""
	print('starting')
	a = AStar_Solver(string,goal)
	a.Solve()
	for i in rnage(len(a.path)):
		print("%d) " %i + a.path[i])
