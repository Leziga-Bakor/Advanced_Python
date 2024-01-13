import numpy as np

b=np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]
    ]
)

print(b.min())
print(b.max())
print(b.mean())
print(b.std())
print(b.sum())
print(np.median(b))