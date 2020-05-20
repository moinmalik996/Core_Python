from numpy import *

rows = int(input("Enter No. Of Rows     :  "))
clms = int(input("Enter No. OF Columns  :  "))

new_array = zeros((rows, clms), dtype=int)

_len_rows = len(new_array)

for outer in range(_len_rows):
    for inner in range(len(new_array[outer])):
        value = int(input("Enter Values To 2D-Array  :  "))
        new_array[outer][inner] = value

print("\nArray is :  ")
print(new_array)
print("\n")

for x in range(_len_rows):
    for z in range(len(new_array[x])):
        print("Row : ", x, "Column : ", z)
        print(new_array[x][z])
