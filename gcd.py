
def gcd(n,m):
    if n%m==0:
        return m
    else:
        return gcd(m,n%m)
print(gcd(54,12))
        
