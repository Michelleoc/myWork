# messing with functions
# variable scope
# Author : Michelle O'Connor

var = 10

def cube(num):
    var = 66
    print ("in function var is ", var)
    return num **3


cube(22)
print ("outside function var is ", var)

# this shows variable scope

