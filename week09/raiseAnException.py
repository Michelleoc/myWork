# Demostrate raising an exception
# This program prompts the user for a number and returns the number multiplied by 2
# Author : Michelle O'Connor

try:
    inputVar = input ("enter a number:")
    number = int(inputVar)
    if (number < 0):
        raise ValueError ("negative value entered")
    print ("Number multiplied by 2 is : ", number *2)
except ValueError as e:
    print ("Please enter a positive number")
    print (e)
