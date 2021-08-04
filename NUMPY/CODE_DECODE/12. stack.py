"""
numpy.stack(array1, array2)
-> It will join two 2d arrays in one array rather than 
concatenating their elements

"""

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print(a)
print( b)

print(np.stack((a, b), axis=1))