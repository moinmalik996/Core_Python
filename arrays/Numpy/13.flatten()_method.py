"""
flatten() method is used to convert 1D to 2D and 3D, 2D to 1D and 3D vice verca

"""

from numpy import *

my_array = array([101, 102, 103, 104, 105, 106, 107, 108, 109])

array_2d = reshape(my_array, (3, 3))  # convert into 3 rows 3 columns ( 1d to 2d )

print("\n1D to 2D using reshape() function\n")

print(array_2d)

print("\n2D to 1D Conversion Using flatten() method\n")

my_array = array_2d.flatten()

print(my_array)


my_array = array_2d