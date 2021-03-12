# Function to take in number and overwrites a file with that number
# Author : Michelle O'Connor

filename = "count.txt"

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))
        
writeNumber (1245621)