import subprocess
import sys
import urllib.request
import os
def check_language(language):
    #checks if the language input is valid. If invalid,program quits
    accepted=["c", "cc", "java", "ml", "pascal", "ada", "lisp", "scheme", "haskell", "fortran", "ascii", "vhdl", "perl", "matlab", "python", "mips", "prolog", "spice", "vb", "csharp", "modula2", "a8086", "javascript", "plsql"]
    if language not in accepted:
        print("language not accepted")
        quit()
################
#Take user input
################
lang=input("enter language ")
check_language(lang)
files=input()
print("Enter name of files or path")
#files.append(input())
infiles=[]
for path,subdirs,files in os.walk(files):
    for filename in files:
        f=os.path.join(path,filename)
        infiles.append(f)
print(infiles)
infiles=infiles[1:]
infiles=infiles[:-1]
for i in infiles:
    for j in infiles:
        if i!=j:
            perl_script=subprocess.check_output(["C:\\cygwin64\\bin\\perl","C:\\Users\\Arushi Chauhan\\Documents\\moss_sub_script.pl",'-l',lang,i,j])            
            l=perl_script.decode("utf-8").split()
            #print(l)
            fp=urllib.request.urlopen(l[-1])
            mb=fp.read()
            web_string=mb.decode("utf-8")
            fp.close()
            l2=web_string.split()
            #print(l2)
            pos=l2.index('<TD')
            pos2=pos-4
            #print(l2[pos+1])
            final_string=l2[pos-1]
            per2=l2[pos2]
            pos=final_string.index('<')
            pos2=per2.index('<')
            #############
            #final result
            #############
            final_string=final_string[:pos]
            print("percentage similarity for ",i,j,final_string,per2[:pos2])
