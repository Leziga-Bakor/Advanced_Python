import numpy as np

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]#

a1 = np.array(l1)
a2 = np.array(l2)

print(l1*5) # repeats list n times
print(a1*5) # muliplies each item in list by n

print(l1+l1) # This concatenates two lists
print(a1+5) # Adds 5 to individual list items