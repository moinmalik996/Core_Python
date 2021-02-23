"""

if two arrays have dissimilar no. of elements
we broadcast smaller array to larger array

Broadcasting have two rules :
Shape is Different 
Either one array have 1-dimension

"""

import numpy as np

arr0 = np.ones((3, 3), dtype='int')

arr1 = np.array([1, 2, 3])

print(arr0.shape)
print(arr1.shape)

