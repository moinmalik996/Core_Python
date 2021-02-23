# np.zeros()_____Enable us to create array of only zeros_____

#  ---> Enables us to identify the exact dimesions of the array
#  ---> Enables us to specify the exact data type

import numpy as np

zeros1 = np.zeros(4, dtype='int')  # will create single dimension array
zeros2 = np.zeros((2, 4), dtype='complex')

print("\nSingle dimension array with 0s")
print(zeros1)
print("\nDouble dimesion array with 0s")
print(zeros2)