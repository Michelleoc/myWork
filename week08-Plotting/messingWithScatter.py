# messing with scatterplots
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, label = "xsquared")
plt.plot (xpoints, xpoints, label = "straight", color = "red")
plt.legend()

randompoints = np.random.randint (1, 10000, 100)
plt.scatter (xpoints, randompoints, label = "random", color = "green")

plt.show () 

