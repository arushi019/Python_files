#Arushi Chauhan 2016019
from studentRecord import *
def readrecords(filename):
    fo=open(filename,"r")
    l=fo.read()
    l=l.split()
    oblist=[]
    index=len(l)
    x=0
    while x!=index:
        s=Student(l[x],l[x+1],l[x+2],l[x+3],l[x+4])
        #print(l[x],l[x+1],l[x+2],l[x+3],l[x+4])
        oblist.append(s)
        x=x+5
    return oblist
def order_records(slist):
    """for x in range(len(slist)):
        for y in range(len(l1)):
            if slist[x]!=l1[y]:
                if slist[x].comes_before(l1[y]):
                    l1.append(slist[x])
                    break"""
    l1=slist
    for x in range(len(l1)-1,0,-1):
        for y in range(x):
            if l1[y].comes_before(l1[y+1])==False:
                temp=l1[y+1]
                l1[y+1]=l1[y]
                l1[y]=temp
    for x in range(len(l1)):
        print(l1[x].RollNo,l1[x].FirstName,l1[x].LastName,l1[x].Program,l1[x].CGPA)
order_records(readrecords("studentdata.txt"))
def display_ordered_data(orderedlist):
                            for x in range(len(orderedlist)):
                                print(orderedlist[x].RollNo,orderedlist[x].FirstName,orderedlist[x].LastName,orderedlist[x].Program,orderedlist[x].CGPA)
   
    
