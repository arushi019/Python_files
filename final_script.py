#!/bin/python3
import subprocess
import sys
import urllib.request
import mosspy
import os

userid = "80676590" # <==== Enter your MOSS user id here.
pathprefix = os.path.abspath(__file__)[:-len(__file__)] # This will point to the directory containing this file. The script assumes the SIM and JPlag files are relative to this

def check_language(language):
    #checks if the language input is valid. If invalid,program quits
    accepted=["java17", "java15", "java15dm", "java12", "java11", "python3", "c", "c++", "text",]
    if language not in accepted:
        print("language not accepted")
        quit()
################
#Take user input
################
if __name__=='__main__':

    ####
    # Use command line arguments  to execute this script
    #   Example command : python3 jplagRunner.py java17 ./Codes/Case1v5/
    # The languages accepted are checked in the check_language() function
    # Invalid invocation results in a usage message being displayed.
    ####

    if(len(sys.argv) != 3):
        print("Usage: python3 jplagRunner.py <language> <directory_location>")
        print("\t<language> : ","java17", "java15", "java15dm", "java12", "java11", "python3", "c", "c++", "text")
        print("\t<directory_location> : The location where all code files are present, relative to this python file. Subdirectories are not scanned.")
        print("NOTE: Ensure that you have JAVA >= 1.7 installed and configured correctly in order for JPlag to work !")
        quit()

    lang=sys.argv[1]
    files=sys.argv[2]
    jplag_files=sys.argv[2]
    check_language(lang)
    moss_lang=lang
    sim_lang=lang
    if files[-1]!='/':
        files=files+'/'
    files=files+"*."
    if lang=="java17" or lang=="java15" or lang=="java15dm" or lang=="java12" or lang=="java11":
        files=files+"java"
        moss_lang="java"
        sim_lang="java"
    elif lang=="python3":
        files=files+"py"
        moss_lang="python"
        sim_lang="disable"
    elif lang=="c":
        files=files+"c"
        moss_lang="c"
        sim_lang="c"
    elif lang=="c++":
        files=files+"cpp"
        moss_lang="cc"
        sim_lang="c++"
    else:
        files=files+"txt"
        moss_lang="ascii"
        sim_lang="text"
    #######
    #MOSS
    #######
    m = mosspy.Moss(userid, moss_lang)    
    # Submission Files
    m.addFilesByWildcard(files+"*")
    if(userid == ""):
        print("Cannot Run Moss Script without user id ! Enter the id in the automation file.")
    else:
        l = m.send() 
        #print(l)
        fp=urllib.request.urlopen(l)
        mb=fp.read()
        web_string=mb.decode("utf-8")
        fp.close()
        l2=web_string.split()
        #print(l2)
        pos_start=l2.index('<TABLE>')
        pos_end=l2.index('</TABLE>')
        file_ptr=pos_start+6
        per_ptr=pos_start+7
        print("\nMOSS Results")
        while per_ptr<pos_end:
            temp_file_name1=l2[file_ptr].split('>')[1]
            temp_file_name2=l2[file_ptr+3].split('>')[1]
            file_ptr=file_ptr+8
            temp_per1=l2[per_ptr].split('<')[0]
            temp_per2=l2[per_ptr+3].split('<')[0]
            per_ptr=per_ptr+8
            print(temp_file_name1,temp_per1,temp_file_name2,temp_per2)
    print("--------------------------------------------------------------------------------")

    ######
    #SIM
    ######
    if sim_lang!="disable":
        sim_string=pathprefix+"SIM/sim_"+sim_lang+".exe"
        temp=subprocess.check_output([sim_string,"-pe",files])
        string=temp.decode("utf-8").split()
        sim_ptr=len(string)-1
        sim_results=''
        while string[sim_ptr]!='tokens':
            if string[sim_ptr]!='material':
                sim_results=string[sim_ptr]+" "+sim_results
            else:
                sim_results='\n'+sim_results
            sim_ptr=sim_ptr-1
        print("\nSIM Results")
        print(sim_results)
    else:
        print("\nSIM results not available for Python")
    print("-------------------------------------------------------------------------------")


    ########
    #JPLAG
    ########
    jplag_string=pathprefix+"JPlag/jplag-2.11.9-SNAPSHOT-jar-with-dependencies.jar"
    temp=subprocess.check_output(["java","-jar",jplag_string,"-vq","-l",lang,jplag_files])
    output = temp.decode("UTF-8")
    i = output.find("submissions")
    jplag_results = output[i+12:-1]
    print("JPlag Results")
    print (jplag_results)
    print("\n\n")
