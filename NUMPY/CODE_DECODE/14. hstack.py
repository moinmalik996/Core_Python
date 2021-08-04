"""
It will stack the elements along Horizontal

"""

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print(a)
print(b)

print(np.hstack((a, b)))