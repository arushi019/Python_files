def sum_digits(n):
    st=str(n)
    st1=[]
    for x in st:
        st1.append(x)
    #print(st1)
    sum=0
    for y in st1:
        y=int(y)
        sum=sum+y
    return sum
def recursive_sum(n):
    while sum_digits(n)>9:
        k=sum_digits(n)
        n=sum_digits(k)
    return n
#print(recursive_sum(56789))
