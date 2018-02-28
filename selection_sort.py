def sel_sort(a):
    for i in range(len(a)):
        small=min(a[i:])
        k=a.index(small)
        temp=a[i]
        a[i]=a[k]
        a[k]=temp
    print(a)
b=[1,3,7,9,2,0,5,4]
sel_sort(b)

