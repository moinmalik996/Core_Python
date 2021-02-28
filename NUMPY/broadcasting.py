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

# 2D arrays with different shape
# Conditions
# 1. Same no. of Dimensions
# 2. Check from right side of their shape (Either equal or one of them is 1) 
a = np.array([   # (4, 2)
    [1, 2],
    [4, 5],
    [7, 8],
    [1, 9]
])

b = np.array([   # (4, 1)
    [9],
    [8],
    [5],
    [8]
    
])

c = a - b  # Will Give an error
print(c)