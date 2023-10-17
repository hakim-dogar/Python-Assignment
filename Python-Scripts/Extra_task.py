import os
import sys

def printingforARGV(start, incremental, ending):
    i=start
    while (i <= ending):
        print(i)
        i+=incremental 


if(sys.argv[1] == "-h"):
    print("Help Manual")
    print("Give arguments during execution of script")
    print("1 argument will display 1 to the argument value")
    print("2 arguments will display numbers starting form 1st arugement to 2nd argument")
    print("3 arguments will display the numbers with increment of 2nd argument with start from 1st argument to the 3rd argument.")
    sys.exit()
elif (len(sys.argv)-1 == 1):
    printingforARGV(1,1,int(sys.argv[1]))
elif (len(sys.argv)-1 == 2):
    printingforARGV(int(sys.argv[1]),1,int(sys.argv[2]))
elif (len(sys.argv)-1 == 3):
    printingforARGV(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
else:
    print("Error, no or more than three arguments passed")
    print("Please send -h for help")