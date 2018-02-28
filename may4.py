n=int(input())
k=int(input())
p=int(input())
i=0
t=[]
for i in (0,n):
    temp=int(input())
    if temp==1:
        t.add(i)
    i=i+1
print(t)
