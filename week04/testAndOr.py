# messing with ands and ors
# Author : Michelle O'Connor

number = 77
if (number >= 0) and (number <=100):
    print ("valid") 

number2 = -1
if (number2 <=0) or (number2 >=100):
    isbad = True
    print ("stop")
else:
    isbad = False
    print ("go")
