k=int(input())
g=int(k/7)
n=7*g
sum=19*n-10*g
r=k%7
if (r==1):
    sum=sum+2
if (r==2):
    sum=sum+7
if (r==3):
    sum=sum+15
if (r==4):
    sum=sum+25
if (r==5):
    sum=sum+38
if (r==6):
    sum=sum+54
print(sum)

