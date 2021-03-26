# see if a file exists
# Author : Michelle O'Connor

import os

filename = "amIHere.text"

if (os.path.exists(filename)):
    print ("file exists")
else:
    with open (filename, "x") as f:
        print ("creating the file")