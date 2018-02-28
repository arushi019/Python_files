t=int(input())
for i in range(t):
    s=input()
    ls=s.split("#")
    day=0
    max=0
    for x in ls:
        if len(x)>0:
            if len(x)>max:
                max=len(x)
                day=day+1
    print(day)
