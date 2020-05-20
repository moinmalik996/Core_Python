"""
reshape() function is used to convert 1D to 2D and 3D, 2D to 1D and 3D vice verca

reshape(array_name, (n, r, c))
array_name = array whose elements to be Converted
n = no. of arrays in resultant array
r = no. of rows  in resultant array
c = c is the no. of columns

"""

from numpy import *

my_array = array([101, 102, 103, 104, 105, 106, 107, 108, 109])

array_2d = reshape(my_array, (3, 3))  # convert into 3 rows 3 columns ( 1d to 2d )

print("\n1D to 2d Conversion\n")

print(my_array)
print("\n")
print(array_2d)

my_new_array = reshape(array_2d, 9)

print("\n2D to 1D Conversion\n")

print(my_new_array)
