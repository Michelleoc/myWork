# Make a list called salaries that hs 10 random numbers between 20000 and 80000 
# But the list stays the same each time you run it
# Author: Michelle O'Connor

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# useful for debugging
