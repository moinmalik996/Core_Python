# It compares element of each array with same index and return the value as TRUE or False

from numpy import *

array_1 = array([101, 102, 103, 104, 105])
array_2 = array([101, 13, 1, 104, 105])

c = array_1 == array_2

print(c)
