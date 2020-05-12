from numpy import *

array_1 = array([101, 102, 103, 104, 105])
array_2 = array([101, 102, 103, 104, 105])


array_1 = array_1 + 5     # add 5 to each element

for el in array_1:
    print(el)

array_1 = array_1 - 5

print("\n After -5 \n")

for el in array_1:
    print(el)
    
    
print("\n Adding Array-1 and Array_2 \n")

for el in array_1+array_2:
    print(el)

