# messing with numpy
# Author : Michelle O'Connor

import numpy as np 

listOfNumbers = [1,2,3,6]
numbers = np.array([1,2,4,5])

# listofNumbers = listofNumbers +3 - invalid will not work

numbers = numbers +3
# can also do multiply 

numbers = numbers * np.array([1,4,5,6])
# another way of doing multiplication 

print (listOfNumbers)
print (numbers)

randomNumbers = np.random.randint(100, 200, 10)
print (randomNumbers)

randomNumbers = np.random.normal(size = 100)
print (randomNumbers)