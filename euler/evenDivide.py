import fractions
n=20

def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans 

	
print(lcm(n))
