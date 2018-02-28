#Arushi Chauhan
#2016019
#Section-A
#Kunal Dahiya
#2016156
#Section-A
def swapRow(A,row1,row2):
    #working ok
    l1=A[row1]
    A[row1]=A[row2]
    A[row2]=l1
    return A
def Row_Transformation(A,x,row1,row2):
    #working ok
    for y in range(len(A[row1])):
        A[row2][y]=A[row2][y]+x*A[row1][y]
    return A
def make_col_zero(B,ii):
    #function is to make all elements under pivot element 0
    #this construct is executed every time one column is made pivot
    """for k in range(len(B)):
        nonzero_index=[]
        for x in B:
            for y in x:
                if y!=0:
                    nonzero_index.append(y)
                    break"""
    flag=-1
    for x in range(len(B[ii])):
        if B[ii][x]!=0:
            flag=x
            break
    for x in range(ii+1,len(B)):
        if flag!=-1:
            B=Row_Transformation(B,-1*float(B[x][flag]/B[ii][flag]),ii,x)
    return B
def get_me_step3(B):
    #finally this function will be called and not make_col_zero
    for n in range(len(B)-1):
        B=make_col_zero(B,n)
    return(B)
def divide_step4(B,n1):
    #make pivot elements one
    for x in B[n1]:
        if x!=0.0:
            flag=x
            #print(flag)
            break
    for k in range(len(B[n1])):
        B[n1][k]=float(B[n1][k]/flag)
    return(B)
def get_me_step4(B):
    for x in range(len(B)):
        for y in range(len(B[x])):
            if B[x][y]!=0:
                B=divide_step4(B,x)
    return B
def make_col_zero_up(B,n1):
    flag=-1
    for x in range(len(B[n1])):
        if B[n1][x]==1 or B[n1][x]==1.0:
            flag=x
            break
    for k in range(0,flag):
        B=Row_Transformation(B,-1*float(B[k][flag]/B[n1][flag]),n1,k)
    return B
def get_me_step5(B):
    #finally this function will be called and not make_col_zero_up
    for k in range(len(B)):
        B=make_col_zero_up(B,k)
    return B
"""def get_me_rank(B):
    rank=0
    for x in range(len(B)):
        for y in range(len(B[x])):
            if B[x][y]==1.0 or B[x][y]==1:
                rank+=1
                continue
    return rank"""
def MatrixRank(A):
    B=get_me_step3(A)
    C=get_me_step4(B)
    D=get_me_step5(C)
    rank=0
    for x in range(len(D)):
        for y in range(len(D[x])):
            if D[x][y]==1.0 or D[x][y]==1:
                rank+=1
                continue
    return rank
    """how to proceed:
    1.check if A[0][0]=0. If yes then swap with the row having nonzero first element
    2.make all elements in column[0]==0
    3.save the matrix
    4.now check for A[1][1]. repeat steps 1-3"""
    """#iterate over each row
    for x in range(len(A)):
        B=A
        #check if the xth index is 0
        k=x
        while k!=len(A)-1:
            flag=0
            if A[x][k]==0:
                #if yes, swap with next immediate row having xth index non zero
                for y in range(x+1,len(A)):
                    if A[y][k]!=0:
                        B=swapRow(B,y,x)
                        break
                #if not check for x+1th index
            k=k+1
        #print(B)"""
    """for x in range(len(A)):
        flag=0
        for k in range(len(A[x])):
            if B[x][k]!=0:
                flag=1
                index=k
                print(index)
                for t in range(x+1,len(A)):
                    B=Row_Transformation(B,-1*float(B[t][index]/B[x][index]),x,t)
                    print(B)
                    print(x,"-->",t)
                flag=0"""
    #B is my swapped matrix
    #make all elements under first non zero element in B zero
    #kaun padhega diode
    #print(B)
    """for y in B[x]:
        if y!=0:
            flag=y
            break
        flag=int(flag)
    for t in range(x,len(B)):
        #print(float(A[t][flag]/A[x][flag]))
        B=Row_Transformation(B,(float(A[t][flag]/A[x][flag])),int(x),int(t))"""
    return B
#a=[[3,3,4,5],[1,1,0,3],[1,1,-1,3],[-1,2,4,2],[6,1,-1,3]]
#b=get_me_step3(a)
#print(b)
#c=get_me_step4(b)
#print(c)
#print(make_col_zero_up(c,2))
#d=get_me_step5(c)
#print(MatrixRank(a))
#print(MatrixRank([[3,3,4,5],[1,1,0,3],[1,1,-1,3],[-1,2,4,2],[6,1,-1,3]]))
