import numpy as np

arr0 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr0.flatten(order='F'))
print(arr0.flatten(order='C'))

arr1 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15]
        
    ]
])

print(arr1.flatten(order="F"))