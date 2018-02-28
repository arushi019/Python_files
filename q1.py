def series(l,n):
    if n==1:
        return l
    elif n%2==0:
        n=n//2
        l.append(n)
        return series(l,n)
    else:
        n=n*3+1
        l.append(n)
        return series(l,n)
i=int(input(''))
j=int(input(''))
lent=[]
for k in range(i,j+1):
    print(series([k],k))
    lent.append(len(series([k],k)))
print(max(lent))
    
