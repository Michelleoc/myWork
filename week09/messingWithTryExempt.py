# This program is to show how you can try exempt
# Author : Michelle O'Connor


import sys

# print (sys.argv)
filename = sys.argv[1]

try:
    with open(filename) as f:
        print (f.read()) 
    var = 10/0
except FileNotFoundError:
    print("File does (", filename,") does not exist", sep="")
    # print(e)
# except:
    # print("an exception occured")
    # not a very effective way of identifying an error as it does not tell you what the error is

print("the end")