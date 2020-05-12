# where() method is used to create an array depend upon a condition.
# array_name = where(condition, expresion_1, expression_2)
# if condition is True expresion_1 will be executed
# if condition is False expression_2 will be executed
# It compares two arrays

from numpy import *

array_1 = array([101, 10, 10, 10, 105])

array_2 = array([100, 103, 1, 24, 10])

check = where(array_1 > array_2, array_1, array_2)

print(check)
