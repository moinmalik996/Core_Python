#  this method is used to delete the last element of array
# array_name.pop()
# array_name.pop(index)

from array import *

stu_roll = array('i', [12, 13, 14, 15, 16])

for el in stu_roll:
    print(el)

# Index Not Specified
stu_roll.pop()

print("\nPop Without Index\n")

for el in stu_roll:
    print(el)

# Index Specified
stu_roll.pop(2)

print("\nPop With Index\n")

for el in stu_roll:
    print(el)

