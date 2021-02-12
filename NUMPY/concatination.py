import numpy as np


a = np.array([
    [1, 2],
    [4, 5]
])

print(a)

b = np.array([
    [7, 8]
])

c = np.concatenate((a, b.T), axis=1)
print(c)