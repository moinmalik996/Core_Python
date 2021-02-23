import numpy as np


arr = np.array([100, 200, 300, 400, 500, 600, 700])
print(arr)

indexes = np.array([1, 2, 3, 4])

print(arr[indexes])
# print(arr[1, 2, 3])  There will be an error

indexes = [0, 2, 4, 6]
print(arr[indexes])

# Indexing for 2D arrays
print("\nIndexing For 2D-Arrays.\n")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2[[0, 1, 2], [1, 2, 1]])  # [0, 1]  for rows of elements
                                   # [1, 2]  for columns of elements
                                   

# Boolean Indexing
print("\nBoolean Indexing\n")

print(arr2[arr2 % 2 == 0])