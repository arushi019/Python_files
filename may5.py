import copy
ct=0
def rec(b,a,pro,pt,k,n):
    j=0
    s=0
    global ct
    while j<n:
        if b[j]==True:
            s=s+2**j
        j=j+1
    if s not in d:
        d.append(s)
        if pro>k:
            ct=ct+1
    if pt<n:
        b1=copy.deepcopy(b)
        b1[pt]=True
        rec(b,a,pro,pt+1,k,n)
        rec(b1,a,pro*a[pt],pt+1,k,n)
num=list(map(int,input().split()))
n1=num[0]
k1=num[1]
a1=list(map(int,input().split()))
d=[]
b2=[False]*n1
rec(b2,a1,1,0,k1,n1)
print(2**n1-ct-1)

        
