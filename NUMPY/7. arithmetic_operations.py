import numpy as np


arr = np.array([1, 2, 3, 4,5])
print(arr * 3)
print(arr - 3)
print(arr + 3)
print(arr % 3)
print(arr ** 2)

print("\nAdding Elements of two Arrays")

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

arr3 = arr1 + arr2

print(arr3)
print("\nAdd np.add(array1, array2) method")
print(np.add(arr1, arr2))
