"""

arr[start:stop:step]

"""

import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr)

print(arr[0:9:2])  # for 1D-Array

arr1 = np.array([
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
])

print("\n")

print(arr1[1:2, 0:2])   # 1:2 means just 1st row
                        # 0:2 means 1st and 2nd Column

print("\n", arr1)
print("\nprint 4 and 6 from the array : ")                  
print(arr1[1:2 , 1:])


# 3D Array Slicing


arr3 = np.array([                # i
    [                            # j
        [1, 2, 3, 4],            # k
        [6, 7, 8, 9],
        [0, 3, 5, 7]
    ],
    [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [9, 8, 7, 6]
    ]
])

print("\nThis is a 3D-Array.\n")
print(arr3)

print("\nSlicing of 3D-Array.\n")
print(arr3[ : , : , 3: ])
print(arr3[0:1, 1:2, 0: ])  # 0:1 for 1st big array
                             # 1:2 for its Row
                             # 0:  for its columns

                        



