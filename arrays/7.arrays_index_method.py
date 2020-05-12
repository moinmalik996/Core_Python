# index method used to find the index of the element
# if element occur more times then it will give index of 1st occurrence
# array_name.index(element)

from array import *

stu_roll = array('i', [10, 20, 30, 40, 20, 50])

print("\nArray\n")
for el in stu_roll:
    print(el)

# Apply index Method _ Only give index of the 1st Occurrence
print("\nFind Index\n")

find_index = stu_roll.index(50)

print("\nThe Index Of ", stu_roll[find_index], " is ", find_index)








