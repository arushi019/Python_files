data_form=[["ID","Status","Price"],["Integer","Character","Float"],[5,20,10]]
file=open("A:/in.txt","r")
string=file.read()
ls=string.split('\n')
final_ls=[]
for i in ls:
    final_ls.append(i.split(','))
print(final_ls)

    
file.close()
