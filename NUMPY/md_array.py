import numpy as np

a = np.array([[1, 1, 2],
              [2, 2, 3],
              [3, 3, 4]])

print(a)
print(a.shape) # Tells the no. of Rows and Columns

# Acess Elements in Multidimentional Array
print(a[0][0])
print(a[0][1])
print(a[0][2])

# Print the whole Column
print("\nPrint a particular Column")
print(a[:,1])

# Print the whole Row
print("\nPrint a particular Row")
print(a[1,:])

# Transpose of Array
print("\nTranspose Of Array :  ")
print(a.T)

# Inverse Of Square Matrix
a = np.array([
              [6, 6],
              [2, 1]
            ])
print("\nInverse of Square Matrix.")
print(np.linalg.inv(a))

# Determinant Of Square Matrix
print("\nDeterminanat of Square Matrix.")
print(np.linalg.det(a))

a = np.array([
    [1, 2, 3],
    [4, 1, 7],
    [0, 10, 0]
])

# Checking Conditions on Array Elements
print("\nChecking Bool Conditions on Array Elements")
bool_index = a <= 2
print(bool_index)
print(a[bool_index])

# Where Method
print("\nnp.where(condition, array, default_number for False Condition)")
b = np.where(a % 2 == 0, a, 0)
print(b)

# ArgWhere Method
print("\nnp.argwhere(condition).flatten()")
b = np.argwhere(a % 2 == 0).flatten()  # Flatten is used to convert 2D in 1D
print(b)
