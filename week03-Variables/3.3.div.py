# A program that reads in two numbers and divides the first number by the second number and give the integer result and the remainder
# Author : Michelle O'Connor

firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter the number you want to divide by: "))
answer = int(firstnumber // secondnumber)
remainder = firstnumber % secondnumber

print("{} divided by {} is {} with a remainder {}".format(firstnumber, secondnumber, answer, remainder))

# learning outcome
# be careful of spaces in the lines, an extra space can cause a syntax error
# be ensure you have the correct number of () in the lines
