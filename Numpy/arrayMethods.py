import numpy as np

a = np.array([1,2,3])
a = np.append(a, [7,8,9])

a = np.insert(a, 3, [4,5,6]) # insert item at a specific position

np.delete(a, 1) # Delete item at specified index
np.delete(a, 1, 0)