l=[]
fo=open("EnglishWords.txt","r")
st=fo.read()
st=st.split()
for line in st:
    if line[0]=='t':
        l.append(line)
print(len(l))
