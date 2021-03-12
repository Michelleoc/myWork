# To read a number from a txt file
# Author : Michelle O'Connor

filename = "count.txt"

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber()
print (num)