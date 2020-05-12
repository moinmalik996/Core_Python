# Extend Method is used to add another array or iterable object at the end of array
# array_name.extend(another_array)


from array import *

stu_roll = array('i', [10, 20, 30, 40, 20, 50])
stu_roll_1 = array('i', [60, 70, 80, 90])

len_stu_rol = len(stu_roll)
len_stu_rol_1 = len(stu_roll_1)

print("\n Stu_rol \n")
for x in range(len_stu_rol):
    print(x, ". ", stu_roll[x])


# Extending stu_rol
stu_roll.extend(stu_roll_1)
len_stu_rol = len(stu_roll)

print("\n After Extend \n")
for x in range(len_stu_rol):
    print(x, ". ", stu_roll[x])
