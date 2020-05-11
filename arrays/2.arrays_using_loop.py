"""
without index :
for element in array_name:
    print(element)

with index:
array_length = len(array_name)
for element in range(array_length):
    print(element)

"""

from array import *

stu_rol = array('i', [12, 13, 14, 15])

print("\n")

# without Index
for el in stu_rol:
    print(el)

print("\n")

# With Index
length = len(stu_rol)
print(length)
for i in range(length):
    print(i, ". ", stu_rol[i])