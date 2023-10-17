import subprocess

# Logged in User Information
#   For all logged in users, show their names and the time and date of their last login.
#       Hint: use who, lastlog, and parse /etc/passwd.



def CheckDateTime():
    try:
        output = subprocess.check_output(["who"]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

    usrdata = []
    
    lines1 = output.strip().split(" ")
    for line in lines1:
        usrdata.append(line)

    filtereddata = [x for x in usrdata if x != '']

    return filtereddata[0], filtereddata[2], filtereddata[3]

Username, usrDate, usrTime = CheckDateTime()

print ("Username: %s    Date: %s    time: %s" % (Username, usrDate, usrTime))
