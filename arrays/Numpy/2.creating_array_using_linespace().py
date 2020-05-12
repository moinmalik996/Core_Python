"""
Creating array using linespace()
array_name = linespace(start, stop, num, endpoint=True)
if num is not specified then default value of num = 50

"""
from numpy import *

my_array = linspace(1, 8, 5, endpoint=True) # divide 1 to 8 into 5 pieces

print(my_array)

for el in my_array:
    print(el)


