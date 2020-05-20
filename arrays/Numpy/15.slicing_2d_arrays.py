#  Slicing On 2D arrays

from numpy import *

array_2d = array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Get all elements of 2nd _column

new_array = array_2d[ :, 1:2]


print("Basic Array\n")
print(array_2d)

print("\nSlicing Array\n")
print(new_array)












