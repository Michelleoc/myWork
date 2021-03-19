# messing with matplotlib
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, label = "xsquared")
plt.plot (xpoints, xpoints, label = "straight", color = "red")
plt.legend()
# plt.show () to display

plt.savefig("lecture2.png")



