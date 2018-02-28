t=int(input())
for i in range(t):
    ls=input().split()
    #print(ls)
    if len(ls)==1:
        if ls[0][0].islower():
            ls[0]=ls[0][0].upper()+ls[0][1:].lower()
        else:
            ls[0]=ls[0][0]+ls[0][1:].lower()
    elif len(ls)==2:
        if ls[1][0].islower():
            ls[1]=ls[1][0].upper()+ls[1][1:].lower()
        else:
            ls[1]=ls[1][0]+ls[1][1:].lower()
        ls[0]=ls[0][0].upper()+". "
    else:
        if ls[2][0].islower():
            ls[2]=ls[2][0].upper()+ls[2][1:].lower()
        else:
            ls[2]=ls[2][0]+ls[2][1:].lower()
        ls[0]=ls[0][0].upper()+". "
        ls[1]=ls[1][0].upper()+". "
    st=""
    for i in ls:
        st=st+i
    print(st)
                    
                 
