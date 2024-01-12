import numpy as np

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

print(a.shape)
print(a.reshape((5,4)))
print(a.reshape((20)))
print(a.reshape((2,2,5)))

a.resize((10,2))
print(a)

print(a.flatten()) #gives one dimension of array

