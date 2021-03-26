# Program that keeps reading numbers until the user enters a 0
# The porgram should append each of them into a list
# The program should then print out each of the numbers entered and the average of them (Use a list)

# Author : Michelle O'Connor

numbers =  []

number = int(input ("enter number (0 to quit) : )"))

while number != 0:
    numbers.append (number)
    number = int(input ("enter another number (0 to quit) : )"))

for value in numbers:
    print (value)

average = float (sum(numbers)) / len(numbers)

print ("The average is {}" .format(average))