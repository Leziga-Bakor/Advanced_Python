import numpy as np

number = np.random.randint(100)

number = np.random.randint(90, 100, size=(2,3,4))

num = np.random.bionomial(10, p=0.5, size=(5,10))

numbers = np.random.choice([10,20,30,40,50],size=(5,10))

np.save('myarray.npy', a)