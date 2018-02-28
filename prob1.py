t=int(input())
for i in range(t):
    k=int(input())
    s=input()
    l=s.split()
    for j in l:
        j=int(j)
    l.sort()
    
    print(l)
    up=0
    if k%2==0:
        up=k/2
    else:
        up=(k-1)/2
        up=up+1
    ct=0
    error=0
    while(ct<up):
        temp=l[ct]-ct
        temp=temp**2
        error=error+temp
        print(temp)
        ct=ct+1
    while(ct>=0):
        temp=l[k-ct-1]-ct
        temp=temp**2
        error=error+temp
        print(temp)
        ct=ct-1
    print(error)
