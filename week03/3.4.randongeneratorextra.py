# A program to print out a random number between a range selected by the user
# Author : Michelle O'Connor

# source : w3schools.com

import random

start = int(input('Enter start of range : '))
stop = int(input('Enter end of range : '))
number = random.randint (start, stop)

print ("Here is a random number : {} " . format(number))