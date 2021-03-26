# Program to tell user if the number they enter is even or odd
# Author : Michelle O'Connor

number = int(input("Enter an integer : "))

if (number % 2) ==0 : 
    print (" {} is an even number" .format (number))
else:
    print (" {} is an odd number" .format (number))