# Program to show the format of an if and elif statement
# Author : Michelle O'Connor

aNumber = 13
if (aNumber % 2) == 0: # I did not need the brackets, in for clarity, easier to read
    print (aNumber, " is even") # anotehr way of printing variables
elif (aNumber % 3) == 0:  # if the number is even this will not be checked
    print (aNumber, "is divisable by 3" )
else:
    print (aNumber, "is not even or divisable by 3")

print ("this will always be outputted")