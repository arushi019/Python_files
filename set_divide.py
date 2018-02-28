def set_divide(a,r):
    if len(a)==r:
        print(a)
    else:
        for x in range(len(a)):
            a1=a[:x]+a[x+1:]
            set_divide(a1,r)
set_divide([1,2,3,4,5],2)
