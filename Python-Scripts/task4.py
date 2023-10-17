import sys
import subprocess

# Managing Disk Space
#   List, one at a time, all files larger than 100K in the /home/username directory tree. Give the user the option to delete or compress the file, then proceed to show the next one.
#       Write to a logfile the names of all deleted files and the deletion times

def CommandCallback(Comm):
    try:
        output = subprocess.check_output(Comm, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print("Error Occured: ",e)

    return output

def CommandCall(Comm):
    try:
        output = subprocess.check_output(Comm, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print("Error Occured: ",e)

def DiskManagement():
    findcomm=f'find $1 -type f -size +100k'

    filesfound=CommandCallback(findcomm)

    filefound1 = filesfound.strip().split("\n")

    
    for file in filefound1:
        print ("%s is larger than 100KB\n" % file)

        while True:
            invar = input("\nClick '1' to Delete\nClick '2' to Compress\nClick 's' to skip\nClick 'q' to quit\n\n Enter the Option: ")

            if(invar == 'q'):
                print("Exited")
                sys.exit()
            elif(invar == 's'):
                break
            elif (invar == '1'):
                deletecomm=f'rm -f {file}'
                CommandCall(deletecomm)

                print("File %s has been Deleted" % (file))

                deletedfilecom = "deletedfiles.log"
                datecomm=f'date'
                dateTime=CommandCallback(datecomm)
                with open(deletedfilecom, 'a') as filewriting:
                    filewriting.write(file)
                    filewriting.write("    %s"%(dateTime))
                
                print("Deleted File name has been logged\n")
                break
            elif (invar == '2'):
                Compresscom=f'zip "{file}.zip" "{file}"\n'
                CommandCall(Compresscom)

                print("File %s has been zipped\n" % file)
                break
            else:
                print("Invalid Input, please try again\n")


DiskManagement()
