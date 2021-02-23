#  eye() : Return an array filled 
#          with zeros except at k-th
#          diagonal, where values are 1

import numpy as np
 
arr0 = np.eye(2)  # 2 columns 2 rows
arr1 = np.eye(3, 3)

print("\n")
print(arr0)
print("\n")
print(arr1)
print("\n")

arr2 = np.eye(4, 4, k=1)  # by default k = 0
print(arr2)

arr2 = np.eye(4, 4, k=-1)  # by default k = 0
print(arr2)

