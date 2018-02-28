def phone_book():
    fo=open("studentdata.txt","r")
    st=fo.read()
    l=st.split()
    #print(l)
    dt={}
    for x in range(len(l)):
        rem=x%5
        if rem==0:
            dt[l[x]]=l[x+1]
    return dt
def query(dt,val):
    if val in dt.keys():
        print (dt[val])
    else:
        print("not found")
query(phone_book(),'2016001')
