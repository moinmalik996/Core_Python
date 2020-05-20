from numpy import *

my_array = array([[101, 102, 103, 104, 105],
                  [12,  13,  13,  45,  67],
                  [1,    2,   4,   3,   5]])

print(my_array)

find = int(input("Enter The Number You Want In Array  :  "))

print("\n")
array_length = len(my_array)

for outer in range(array_length):
    for inner in range(len(my_array[outer])):
        if find == my_array[outer][inner]:
            print(find, " is found\n", "Row : ", outer, " Column : ", inner)
        else:
            print(find, "is not Present in Array")
            break
    break


