import numpy as np 

'''
# Numpy Array
a = np.array([1,2,3,4,5])

a_mul = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)
'''


# Static typing in numpy
a = np.array([[1,2,3],
              [4, 'Hello', 6],
              [7,8,9]])

print(a.dtype)
