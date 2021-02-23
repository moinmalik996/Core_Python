"""
Attributes of An Array

--> Dimension
--> Shape
--> Size
--> Dtype
--> itemSize

"""

import numpy as np


arr0 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(arr0)

print("\nDimensions of Array  :  ", arr0.ndim)   # Dimesions of the Array

print("\nShape of Array       :  ", arr0.shape)  # no. of rows and columns

print("\n Size of Array       :  ", arr0.size)   # Total No. of Elements (rows x columns)

print("\n Itemsize of Array   :  ", arr0.itemsize)


