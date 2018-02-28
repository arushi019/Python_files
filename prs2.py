import subprocess
import sys
def check_language(language):
    #checks if the language input is valid. If invalid,program quits
    accepted=["c", "c++", "java", "pasc", "m2", "lisp", "mira", "8086"]
    if language not in accepted:
        print("language not accepted")
        quit()
################
#Take user input
################
lang=input("Enter language")
check_language(lang)
files=[]
print("Enter name of file")
files.append(input())
##########################################
#invoke exe file corresponding to language
##########################################
sim_string="C:\\sim_"+lang+".exe"
temp=subprocess.check_output([sim_string,"-pe",files[0]])
###############################################
#capture output and extract required percentage
###############################################
string=temp.decode("utf-8").split()
#print(string)
sim_ptr=len(string)-1
sim_results=''
while string[sim_ptr]!='tokens':
    if string[sim_ptr]!='material':
        sim_results=string[sim_ptr]+" "+sim_results
    else:
        sim_results='\n'+sim_results
    sim_ptr=sim_ptr-1
print(sim_results)

