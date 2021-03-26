# A program that reads in a string and strips any leading or trailing spaces. Also the program converts the string to lower case
# The program will putput the length of the input and output strings.

# Author : Michelle O'Connor

rawString = input("please enter a string")
normalisedString = rawString.strip().lower()

lengthofRawString = len(rawString)
lengthofNormalised = len(normalisedString)

print ("That String normalised is : {}" .format(normalisedString))
print ("We reduced the input string from {} to {} characters" .format(lengthofRawString, lengthofNormalised))