import sys
import os
import subprocess

#Safe Delete
#   Write, as a script, a “safe” delete command, srm.sh.
#   Filenames passed as command-line arguments to this script are not deleted, but instead gzipped if not already compressed (use file to check), then moved to a /home/username/trash directory.
#   At invocation, the script checks the “trash” directory for files older than 48 hours and deletes them.


def CommandCall(Comm):
    try:
        output = subprocess.check_output(Comm, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print("Error Occured: ",e)

def SafeDelete():

    argvfiles=[]

    for arguments in sys.argv:
        if(arguments != sys.argv[0]):
            argvfiles.append(arguments)

    for files in argvfiles:
            filename, fileextension = os.path.splitext(files)

            if (fileextension != ".gz") and (fileextension != ".zip") and (fileextension != ".tar"):

                #Compressing Command Process
                Compresscom=f'gzip "{files}"'
                CommandCall(Compresscom)

                #moving to Trash Command Process
                trashcomm = f'gio trash "{files}.gz"'
                CommandCall(trashcomm)
            else:
                trashcomm1 = f'gio trash "{files}"'
                CommandCall(trashcomm1)


    finddeletecomm = f'find /home/eurus/.local/share/Trash/files -type f -mmin +2880'
    CommandCall(finddeletecomm)

    emptycomm=f"gio remove -f $finddeletecomm"
    CommandCall(emptycomm)

# Main Function call
SafeDelete()