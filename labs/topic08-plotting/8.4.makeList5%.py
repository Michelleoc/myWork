# Make a list called salaries that hs 10 random numbers between 20000 and 80000
# But the list stays the same each time you run it
# Create another array of numbers that has salaries plus 5000
# Increase all salaries by 5% and store in an array
# Author: Michelle O'Connor

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000
print(salariesPlus)
 
salariesMult = salaries * 1.05
print(salariesMult)

# this is a float array to convert to an int array
# newSalaries = salariesMult.astype(int)
