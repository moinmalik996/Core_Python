# Creating 2d arrays

from numpy import *

array_2d = array([ [101, 102, 103, 104, 105],
                   [22,   11,  33,  44,  55] ])

print(array_2d)
n = len(array_2d)

# without index
print("\nWithout Index\n")
for el in array_2d:
    for el_inner in el:
        print(el_inner)
    print("")
    
print("\nWith Index\n")
for x in range(n):
    for el in range(len(array_2d[x])):
        print(array_2d[x][el])
    print("")

