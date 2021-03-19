# Create a list of ages that has the same number random values as salaries
# make a scatter plot
# Author: Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries) 

plt.scatter(ages, salaries ) 
plt.show()