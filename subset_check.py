def checker(l1,l2):
    flag=0
    for x in l1:
        if x not in l2:
            flag=-1
            break;
    return (flag==0)
print(checker([1,2,3],[1,5,6,3]))
