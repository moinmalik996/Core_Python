"""
numpy.concatenate((array1, array2), axis=0, out=None)
-> we cannot concatenate arrays with different dimensions
-> axis = along which the arrays will be joined

"""
import numpy as np


arr0 = np.arange(1, 7).reshape(2, 3)
arr1 = np.arange(7, 13).reshape(2, 3)

print(arr0)
print(arr1)

print()
print(np.concatenate((arr0, arr1), axis=0))
print()
print(np.concatenate((arr0, arr1), axis=1))

