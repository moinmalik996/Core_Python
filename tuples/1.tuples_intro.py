# Tuples : Ordered , Immutable,  Allows duplicates
# same like lists but cannot alter after creation

my_tuple = tuple(["Name", 23, 45.8, False])

print()
print(my_tuple)

print("\n")
print(type(my_tuple))
print("\n")

find = "Name"  # find item in Tuple

if find in my_tuple:
    print("\nPresent")
else:
    print("\nNot Present")



find = "Name"  # find index in tuple

print()
print(my_tuple.index(find))

# convert tuple into list

mylist = list(my_tuple)

print()
print(mylist)

my_new_tuple = tuple(mylist)

print()
print(my_new_tuple)

# assigning tuple items to varialbles

name , age , marks, married = my_tuple

print(name, age, marks, married)