#!/bin/python3
import subprocess
import sys
def check_language(language):
    #checks if the language input is valid. If invalid,program quits
    accepted=["java17", "java15", "java15dm", "java12", "java11", "python3", "c/c++", "c\#-1.2", "char", "text", "scheme"]
    if language not in accepted:
        print("language not accepted")
        quit()

if __name__ == '__main__':
	####
	# Use command line arguments  to execute this script
	# 	Example command : python3 jplagRunner.py java17 ./Codes/Case1v5/
	# The languages accepted are checked in the check_language() function
	# Invalid invocation results in a usage message being displayed.
	####

	if(len(sys.argv) != 3):
		print("Usage: python3 jplagRunner.py <language> <directory_location>")
		print("\t<language> : ","java17", "java15", "java15dm", "java12", "java11", "python3", "c/c++", "c\#-1.2", "char", "text", "scheme")
		print("\t<directory_location> : The location where all code files are present, relative to this python file. Subdirectories are not scanned.")
		quit()
	lang = sys.argv[1]
	files = sys.argv[2]
	jplag_string="A:/jplag-2.11.9-SNAPSHOT-jar-with-dependencies.jar"	# Location of the JPlag File
	
	check_language(lang)
	
	####
	# Execute JPlag using systems Java version (>=1.8)
	####
	temp=subprocess.check_output(["java","-jar",jplag_string,"-vq","-l",lang,files])
	output = temp.decode("UTF-8")
	i = output.find("submissions")
	jplag_results = output[i+12:-1]
	print (jplag_results)
