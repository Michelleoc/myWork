# This program is to show how you can try except
# Author : Michelle O'Connor

# var = 2 + 5

# filename = "data.txt"

import sys

print (sys.argv)
filename = sys.argv[1]

with open(filename) as f:
    print (f.read()) 

# when running python, run as follows
# python .\messingWithExcept.py data.txt
# put the file name at the end 

# This is useful for the weekly task to find the e's