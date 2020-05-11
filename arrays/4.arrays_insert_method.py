# insert method used to enter element at a particular index
# array_name.insert(index, value)

from array import *

student_roll = array('i', [10, 20, 30, 40, 50])

for x in student_roll:
    print(x)


student_roll.insert(1, 15)
student_roll.insert(2, 19)

print("\nAfter Insert Method\n")

for x in student_roll:
    print(x)



