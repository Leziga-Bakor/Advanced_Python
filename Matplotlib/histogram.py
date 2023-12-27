import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20,1.5,1000)
plt.hist(ages, bins=[ages.min(), 18,21,ages.max()])
plt.show()

plt.hist(ages, bins=20,cumulative=True)
plt.show()