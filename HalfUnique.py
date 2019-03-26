from collections import Counter
def solution(T):
	take = []
	freq = dict(Counter(T))
	for e in T:
		if freq[e] == 1:
			take.append(e)
	for i in range(len(T)/2):
		key = max(freq, key=freq.get)
		if freq[key] != 1:
			freq[key] = freq[key]-1
	return len(freq.keys())
        
T=[80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789] # ->
T=[3,4,6,6,7,7,9,9,14] # -> [3,4,7]



solution(T)
