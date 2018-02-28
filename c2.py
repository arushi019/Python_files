t=int(input())
for i in range(t):
    s=input()
    l1=s.split(">")
    l2=s.split("<")
    #print(l1)
    #print(l2)
    max=0
    for it in l1:
        p=len(it)-it.count("=")
        #print(p)
        if p>max:
            max=p
    for it in l2:
        p=len(it)-it.count("=")
        #print(p)
        if p>max:
            max=p
    print(max+1)
