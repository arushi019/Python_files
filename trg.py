import math
def trg(a,b):
    a=int(a)
    b=int(b)
    c=math.sqrt(a**2+b**2)
    a1=a/c
    t1=math.acos(a1)
    t1=t1*180/math.pi
    t2=round(t1)
    if t2>45:
        t2=90-t2
    print (t2)
trg(5,12)
