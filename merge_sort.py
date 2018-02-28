"""def merge_sort(a1,a2,final):
    if len(a1)==1 and len(a2)==1:
        if a1[0]>=a2[0]:
            final.append(a2[0])
        else:
            final.append(a1[0])
        print(final)
    else:
        m1=len(a1)//2
        a11=a1[:m1]
        a12=a1[m1:]
        merge_sort(a11,a12,final)
        m2=len(a2)//2
        a21=a2[:m2]
        a22=a2[m2:]
        merge_sort(a21,a22,final)
merge_sort([1,4,5,7,2,0,6],[9,3,8],[])"""
def merge_sort(a):
    if len(a)==1:
        
