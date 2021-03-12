# check a file exists using os
# Author : Michelle O'Connor

import os

filename = "count.txt"

if not os.path.isfile(filename):
    print ("File does not exist")
    # initialise file here
else:
    print ("File does exist")


# import os

# filename = "count.txt"

# if (os.path.exists(filename)):
    #print ("file exists")
#else:
    #with open (filename, "x") as f:
        #print ("creating the file")