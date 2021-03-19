# This is to demonstrate matplot lib by ploting y = x squared
# Author: Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints)
plt.show()
