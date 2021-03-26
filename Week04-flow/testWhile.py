# messing with while loops
# Author : Michelle O'Connor

# while conditions

# statements

count = 0
while count < 10:
    print (count)
    count += 1

count = 10
while count  >= 0:
    print (count)
    count -= 1
print ("blast off")

val = input ("enter someting (q to quit):")
while val != "q":
    print ("you said: " +val)
    val = input ("q to quit):")
print ("Goodbye")