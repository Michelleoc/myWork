# messing with functions
# flexible arguments
# Author : Michelle O'Connor

print ("hi", 55, 343, [], {}, sep=":")

# flexible number of arguments


def average (*numbers):
    sumof = sum(numbers)
    return sumof /len(numbers)

ave = average (12, 12, 12, 34, 12, 34)
print ("average is ", ave)


# flexible number or named arguments


def fun(arg1 = 0, arg2 = 1):
    # the numbers on the above line will default in if we don't give arg1 or arg2 a number
    return arg1 -arg2

print (fun(arg2 = 10, arg1 = 2))


