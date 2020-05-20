# Getting User Input In 1 dimensional array

from numpy import *

no_of_elements = int(input("Enter No. Of Elements For Array  :  "))

my_array = zeros(no_of_elements, dtype=int)

for x in range(len(my_array)):
    value = int(input("Enter Value Of Element  :  "))
    my_array[x] = value

print("\nYour Array\n")

print(my_array)

for el in range(no_of_elements):
    print(my_array[el])