import sys

# Changing the line spacing of a text file
#    Write a script that reads each line of a target file, then writes the line back to stdout, but with an extra blank line following. This has the effect of double-spacing the file.



file=sys.argv[1]

filecontent=""

with open(file,'r') as filedata:
    for line in filedata:
        filecontent+=(line.strip()+"\n\n")

orgstd=sys.stdout       #storing the stdout variable

with open(file,'w') as inputdata:
    sys.stdout=inputdata        #putting file in stdout variable, any output command will go to file
    print(filecontent)          #writing in file

sys.stdout = orgstd             #restroing std orginal value.