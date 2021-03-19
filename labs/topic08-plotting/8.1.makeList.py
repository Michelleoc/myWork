# Make a list called salaries that hs 10 random numbers between 20000 and 80000
# Author: Michelle O'Connor

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)
