dp=[0]*10000
dp[0]=0
dp[1]=1
dp[2]=7
def rec(n):
    if n<10000 and dp[n]!=0:
        return dp[n]
    else:
        if n<10000:
            dp[n]=(rec(n-1)+(n*(n+1)*(2**(n-2)))%1000000007)%1000000007
            return dp[n]
        else:
            pro=dp[9999]
            for i in range(100000000,n):
                pro=(pro+(i*(i+1)*(2**(n-2))))%1000000007
            return pro
t=int(input())
for i in range(t):
    n=int(input())
    print(rec(n))
