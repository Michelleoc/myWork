# Demonstrate file as part of lecture
# Author : Michelle O'Connor

with open (".\lecture1.txt", "w") as f:
    print ("create a file")

with open ("testdata.txt", "rt") as f:
    data = f.read() # if you want to read in a certain # of characters put it in (), example (10)
    # each row that ends counts one extra character and also each new additional row counts an extra character at the start
    print (data)