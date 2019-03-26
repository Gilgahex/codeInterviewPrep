import collections
#Find best hand given 10 input cards

def IOWrapper(func):
	def wrapper():
		fp = open(0).read()
		for line in fp.split('\n'):
			func(line)
	return wrapper
	

#Boolean, 5 Same Suit 
def Flush(cardList):
    suits = []
    for c in cardList:
        suits.append(c[1])
    counter = collections.Counter(suits)
    return True if max(counter.values()) >= 5 else False

#Royal Flush
def Royal(cardList):
    rankCheck = ['A','K','J','Q','T']
    check = 0
    if Flush(cardList):
        for c in cardList:
            if c[0] in rankCheck:
                check+=1 
        if check == 5:
            return True
        else:
            return False
    else:
        return False
        

def maxKinds(cardList):
	ranks = [c[0] for c in cardList]
	counter = collections.Counter(ranks)
	return max(counter.values())
    
def numPairs(cardList):
    pairs = 0
    ranks = [c[0] for c in cardList]
    counter = collections.Counter(ranks)
    for i in counter.values():
        if i == 2:
            pairs+=1
    return pairs
     

# 5 Ranks Straight In a row
def Straight(cardList):
	
	ranks = []
	lookup = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7 '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    
    for c in cardList:
		if c[0] in lookup:
			ranks.append(lookup[c[0]])
	rank_set = set(ranks)
	rank_range = max(rank_set) - min(rank_set)
	
	if rank_range == 4:
		return True
	else:
		if rank_set = {14,2,3,4,5}:
			return True
	else:
		return False
    
# fullHouse: If One Pairs & 3 Of a Kind
def fullHouse(cardList):
    return True if numPairs(cardList) == 1 and maxKinds(cardList) == 3 else False


#Royal Flush > StraightFlush > 4 of a Kind > Full House > Flush > Straight > 3 of a Kind > 2 Pair > 1 Pair > High Card
@IOWrapper
def maxHand(cardList):
	
	cardList = cardList.split()
	
	if len(cardList) == 0:
		return "Null Input" 
    
	bestHand = "highest-card"
	
	#Royal Flush
	royal = Royal(cardList)

	#Full House, 3 of a kind + 2 pair
	full_house = fullHouse(cardList)

	#Flush
	flush = Flush(cardList)
    
	#Straight
	straight = Straight(cardList)
    
	#StraightFlush
	straightFlush = True if straight and flush else False

	#Pairs: 1,2,3,4
	num_Pairs = numPairs(cardList)
    
	#Kind Max of a Kind
	kinds = maxKinds(cardList)
    
	#Hand Ordering, 
	if num_Pairs == 1:
		bestHand = "one-pair"
	if num_Pairs == 2:
		bestHand = "two-pair"
	if kinds == 3:
		bestHand = "three-of-a-Kind"
	if straight:
		bestHand = "straight"
	if flush:
		bestHand = "flush"
	if full_house:
		bestHand = "full-House"
	if kinds == 4:
		bestHand = "four-of-a-kind"
	if straightFlush:
		bestHand = "straight-flush"
	if royal:
		bestHand = "royal-flush"
    
	hand = cardList[:5]
	deck = cardList[5:]
	print("Hand:",hand, "Deck:", deck,"Best hand:", bestHand)

maxHand()
