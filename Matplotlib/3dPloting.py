import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x,y,z)
ax.set_title("3D Plot")
ax.set_xlabel('Test')
ax.set_zlabel('Height')
ax.set_ylabel('width')
plt.show()