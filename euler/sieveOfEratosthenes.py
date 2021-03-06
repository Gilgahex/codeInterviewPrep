import math 

def get_n_primes(n):
  m = n+1
  numbers = [True] * m #EDIT: faster
  #Prime Check
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

def get_next_prime(target):
    # Using Ramanujan's Approximation for Pi(n) to approximate n
    #Works for Prime>=5
    n = math.ceil(target * math.log(target))
    m = n+1
    numbers = [True] * m #EDIT: faster
    for i in range(2, int(n**0.5 + 1)):
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
        if primes[-1] > target:
            return primes[-1]
        else:
            continue
    

primeList = get_n_primes(1000)
nextPrimes = list(map(get_next_prime,primeList))
print(primeList)

def check():
    for e in range(len(primeList)-1):
        valid = [None]*25
        if primeList[e] == nextPrimes[e-1]:
            valid[e] = True
        else:
            valid[e] = False
    print(valid)
    
        

