import numpy as np

# b=np.array(
#     [
#         [1,2,3,4,5],
#         [6,7,8,9,10],
#         [11,12,13,14,15],
#         [16,17,18,19,20]
#     ]
# )

# np.save('myarray.npy', b)

# a = np.load('myarray.npy')
# print(a)

# a = np.array([[1,2,3,4,5,6],
#               [7,8,9,10,11,12],
#               [13,14,15,16,17,18],
#               [18,19,20,21,22,23]
#               ])

# np.savetxt('myarray.csv', a, delimiter = ",")
a = np.loadtxt('myarray.csv', delimiter=',')
print(a)