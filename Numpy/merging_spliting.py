import numpy as np

# joining and splitting
a1=np.array([[1,2,3,4,5],
             [6,7,8,9,10]])
a2 =(
    [
        [11,12,13,14,15],
        [16,17,18,19,20]
    ]
)

a = np.concatenate((a1,a2))
print(a)
a = np.concatenate((a1,a2),axis=1)
print(a)

a = np.stack((a1,a2))
print(a)