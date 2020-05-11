# One Dimensional Array : 1 Row , Multiple Columns
# It requires Array Module
# array_name = array.array('type_code',[elements]) in case :  Import array
# array_name = array('type_code', [elements])      in case : from array Import *

import array

stu_rol = array.array('i', [1, 2, 3, 4, 5])  # i = integer

print(stu_rol[0])
print(stu_rol[1])
print(stu_rol[2])
print(stu_rol[3])
print(stu_rol[4])

print("\n")

stu_marks = array.array('f', [23.5, 34.7, 89.2, 23.5, 12])

print(stu_marks[0])
print(stu_marks[1])
print(stu_marks[2])
print(stu_marks[3])
print(stu_marks[4])
