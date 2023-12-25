import numpy as np 
import matplotlib.pyplot as plt 

'''
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

plt.scatter(X_data, Y_data, c="red", s=100, marker='*')
plt.show()

'''

years = [2006 + x for x in range(16)]
weights = [80,83,84,85,86,82,81,79,83,
           83,80,82,82,83,81,79]

plt.plot(years,weights,c='g',lw=3, linestyle = '--')
plt.show()

# NB: line plot is the default plot for matplotlib.pyplot
