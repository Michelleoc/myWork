# messing with histograms
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(1)
# to get the plot to show the same numbers each time.
# This is useful when trying to debug

normData = np.random.normal (size = 10)

plt.hist(normData)

plt.show()