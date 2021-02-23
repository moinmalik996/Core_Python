# np.ones()_____Enable us to create array of only ones_____

#  ---> Enables us to identify the exact dimesions of the array
#  ---> Enables us to specify the exact data type

import numpy as np

ones1 = np.ones(4, dtype='int')  # will create single dimension array
ones2 = np.ones((2, 4), dtype='complex')

print("\nSingle dimension array with 0s")
print(ones1)
print("\nDouble dimesion array with 0s")
print(ones2)