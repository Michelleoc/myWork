# Demonstration of a module
# Author : Michelle O'Connor

import datetime as dt

def gethealthdata (person):
    print ("gethealthdata: ", person["firstname"])

def displayperson (person):
    print (person)

if __name__ == "__main__":
    person1 = {
        "firstname" : "Michelle",
        "lastname" : "O'Connor",
        "dob" : dt.date(2010,1,1),
        "Height" : 180,
        "Weight" : 100
    }

displayperson (person1)
gethealthdata (person1)