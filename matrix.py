def matrix(m1,m2):
    m3=[]
    for x in range(len(m1)):
        l=[]
        for y in range(len(m1[x])):
            l.append(m1[x][y]+m2[x][y])
        m3.append(l)
    print(m3)
def matrix_multiply(m1,m2):
    m3=[]
    if len(m1[0])==len(m2):
        for x in range(len(m1)):
            for z in range(len(m2[0])):
                l=[]
                y=0
                sum=0
                while y<len(m1):
                    k=m1[x][y]*m2[y][z]
                    y=y+1
                    sum=sum+k
                l.append(sum)
            m3.append(l)
        print(m3)
    else:
        print("invalid dimaensions")
        
p1=[[1,2,3],[4,5,6],[7,8,9]]
p2=[[7,8,9],[5,6,7],[1,2,3]]
matrix_multiply(p1,p2)
