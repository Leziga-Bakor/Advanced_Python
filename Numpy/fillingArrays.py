import numpy as np 

a = np.full((2,3,4), 9) # given the size, creates an array filling with one value'
# print(a)

a = np.zeros((10,5,2))
# print(a)

a=np.ones((10,5,2))
# print(a)

a = np.empty((5,5,5))
print(a)

# Generate sequence
x_value = np.arange(0, 1000, 5)
print(x_value)

x_values = np.linspace(0,1000,2)
print(x_values)

# Special values
print(np.nan)
print(np.inf) #Infinity

# check for values

print(np.isnan(np.nan))
print(np.isinf(np.inf))