import numpy as np


arr = np.array([1, 2, 3])
l = [1, 2, 3]
print(l)

l = l * 2
print(l)


print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
print(arr.itemsize, end="\n\n")

#print Values with Index 
print(arr)
print(arr[0])
arr[0] = 10
print(arr)

#Array Multiplication

b = arr * np.array([2, 3, 4])
print(b)

#Array Addition
arr = arr + 4
print(arr)
