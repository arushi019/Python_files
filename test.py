def caseul(s):
    u=0
    l=0
    for x in s:
        if x.islower():
            l=l+1
        if x.isupper():
            u=u+1
    print(u,l)
s1=input("Enter a string")
caseul(s1)
