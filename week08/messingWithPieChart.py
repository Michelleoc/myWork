# messing with pie chart
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(["Apples", "Orange", "Bananas"])

numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()