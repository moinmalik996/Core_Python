# nonzero() method is used to determine the index of Non_zero numbers
# new_array_name = nonzero(array)

from numpy import *

array_1 = array([0, 10, 0, 10, 0])

array_2 = nonzero(array_1)

print(array_2)