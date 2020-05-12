# any()  method returns TRUE if any elements at same indexes have same value
# all()  method returns TRUE if all elements at same indexes have same value

from numpy import *

array_1 = array([101, 102, 103, 104, 105])

array_2 = array([101, 13, 1, 104, 105])

array_3 = array([101, 102, 103, 104, 105])

c = array_1 == array_2
d = array_1 == array_3

print("\nArray_1 vs Array_2")
print(any(c))
print(all(c))

print("\nArray_1 vs Array_3")
print(any(d))
print(all(d))
