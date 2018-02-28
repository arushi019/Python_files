t=int(input())
for i in range(t):
    s=input()
    ls=s.split()
    l2=[]
    for x in ls:
        l2.append(eval(x))
    l2.sort()
    #print(l2)
    if l2[len(l2)-1]!=len(l2)-1:
        print(l2[len(l2)-1])
    else:
        l2[len(l2)-1]=0
        l2.sort()
        print(l2[len(l2)-1])
