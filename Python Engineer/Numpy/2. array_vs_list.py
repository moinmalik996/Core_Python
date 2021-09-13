import numpy as np

l1 = [1, 2, 3]
print(l1)

arr = np.array(l1)
print(arr)

l1.append(4)
# arr.append()   #Numpy has no object of append().
print(l1)

#-----------------Addition----------------

l1 = l1 + [4]    # It will just concatenate the two lists
print("\n\n", l1)

arr = arr + 4    # It will add 4 to each element of Array.
print("\n\n", arr)

#----------------Multiplication-----------


l1 = l1 * 2
print("\n\n", l1)


arr = arr * 2
print("\n\n", arr)


