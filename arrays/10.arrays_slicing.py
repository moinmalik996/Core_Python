# Slicing on arrays can be used to retrieve a group of elements from the array
# new_array_name = array_name[start: stop: stepSize]


from array import *

stu_roll = array('i', [10, 20, 30, 40, 20, 50])

print("\n Basic Array \n")
for el in stu_roll:
    print(el)

# Slicing Array
new_array = stu_roll[2:4]  # it will print less than 4

print("\n Sliced Array \n")
for el in new_array:
    print(el)
