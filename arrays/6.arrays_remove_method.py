# Remove method is used to remove 1st occurrence of the element.
# if the element doesn't found , it will give the error
# array_name.remove(value)

from array import *

stu_roll = array('i', [10, 20, 30, 40, 20, 50])

print("\nArray\n")
for el in stu_roll:
    print(el)

# Apply Remove Method _ Only Remove The 1st Occurrence
print("\nAfter Remove\n")
stu_roll.remove(20)
for el in stu_roll:
    print(el)










