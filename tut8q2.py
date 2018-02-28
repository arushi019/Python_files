def get_special_numbers(a,b,c,d):
    l=[]
    for i in range(c,d+1):
        if i%a==0 and i%b!=0:
            l.append(i)
    print(l)
get_special_numbers(3,5,100,150)
