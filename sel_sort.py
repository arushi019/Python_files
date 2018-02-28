def sel_sort(a):
    print(min(a))
    for x in range(len(a)):
        index=a[x]
        k=a[x:]
        print(k)
        mini=min(k)
        temp=a[x]
        a[x]=min
        min=temp
    print(a)
sel_sort([1,3,6,2,4,9,7])
        
