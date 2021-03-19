# Create a list of ages that has the same number random values as salaries
# make a scatter plot
# add a line to this plot that shows y = x2 in a different colour
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

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints, color = "g")

# plt.show()

plt.savefig("8.8.lab.png")