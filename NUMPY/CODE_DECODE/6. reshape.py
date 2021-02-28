"""

Reshape is used ti change the shape of the array without changing the data in the array.
(3, 5) = 15 elements
(5, 3) = (1, 15) = (15, 1)

numpy.reshape(array, shape, order)

"""
import numpy as np
  

arr = np.arange(1, 11)
print(arr, arr.shape)

a = np.reshape(arr, (5, 2))  # Default Order = C  = Row Wise
print(a)

b = np.reshape(arr, (5, 2), order="F")  # Fortran Style = F = Column Wise
print(b)
