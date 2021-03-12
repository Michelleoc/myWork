# Demonstrate file as part of lecture, this shows now to read in a line
# Author : Michelle O'Connor


with open ("testdata.txt", "rt") as f:
    for line in f:
        print("we got : ", line.strip())
        # strip removes all the spaces, character returns and spare lines

with open("output.txt", "wt") as f:
    f.write("blah the blah \n")
    print ("my data", file = f) # can also use print () option to add/write data into the text file

# You can overwrite the data 
# However if I don't want to overwrite the data, you need to use r+ or append a+
# if open something in write mode it will overwrite all data that is currently in the file

# if want to put the new file in a parent directory use ../ example ../output.txt