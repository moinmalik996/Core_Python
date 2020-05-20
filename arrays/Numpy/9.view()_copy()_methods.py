# view() method is used to create new array of existing array with
# different memory locations just like mirror effect. Modification
# in new array effects existing array.

# copy(existing_array)  method is same as view rather the fact that
# they are not like mirror effect and change in new array does not effects
# existing array.


from numpy import *

a = array([101, 102, 103, 104, 105])

b = a.view()

c = copy(a)

print(a)
print("a : ", id(a))
print(b)
print("a : ", id(b))

print("\nAfter Alteration in b\n")

b[1] = 99  # it will effect a

print(a)
print(b)

print("\n")

print(a)
print("a : ", id(a))
print(b)
print("c : ", id(c))

print("\n")

c[3] = 80  # it will not effect a

print(a)
print(c)










