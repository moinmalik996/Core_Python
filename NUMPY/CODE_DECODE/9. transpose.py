import numpy as np

arr0 = np.arange(1, 25).reshape(2, 3, 4)
print(arr0, arr0.shape)

print("\n")

arr1 = np.transpose(arr0)
print(arr1, arr1.shape)  # it will be (4, 3, 2)

arr2 = np.transpose(arr0, axes=(1, 2, 0))
print(arr2, arr2.shape)