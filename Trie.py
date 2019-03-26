class Trie:
	head = {}
	
	def add(self,word):
		cur = self.head
		for c in word:
			if c not in cur:
				cur[c] = {}
			cur = cur[c]
		cur['*'] = True
	
	def search(self,word):
		cur = self.head
		for c in cur:
			if c not in cur:
				return False
			cur  = cur[c]
		if '*' in cur:
			return True
		else:
			return False
			
aTrie = Trie()
aTrie.add("word")
aTrie.add("words")
aTrie.add("worthy")

print(aTrie.search("worthy"), aTrie.search("worth"), aTrie.search("wealth"))


