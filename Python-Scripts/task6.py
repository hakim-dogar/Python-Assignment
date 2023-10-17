import subprocess
import os

# Write a script which will test how many logins you and the ‘root’ user have and tell  who has the most (or if equal)

def get_currentuser_ROOT_loginCount():

    usercomm='grep -c "session opened for user eurus" /var/log/auth.log'
    rootcomm='grep -c "session opened for user root" /var/log/auth.log'

    try:

        usertimes = subprocess.check_output(usercomm, shell=True,stderr=subprocess.STDOUT, text=True)

        roottimes= subprocess.check_output(rootcomm, shell=True,stderr=subprocess.STDOUT, text=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

    return usertimes, roottimes
    

usercount, rootcount = get_currentuser_ROOT_loginCount()

currentuser = os.getlogin()

print("%s has login numbers %s" % (currentuser, usercount))
print("Root has login numbers %s" % (rootcount))

if usercount == rootcount:
    
    print("%s and root has same login count" % (currentuser))
elif usercount > rootcount:
    print ("%s has more logins than root"% (currentuser))
else:
    print("Root has more logins than %s" % (currentuser))