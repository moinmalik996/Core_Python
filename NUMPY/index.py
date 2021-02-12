import numpy as np

print(np.__version__)

a = np.array([1, 2, 3])
print(a)

# Basic Information
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

print("\n\n")
print(a[0])
a[0] = 12
print(a)

b = a * np.array([2, 4, 6])
print(b)

# Difference between array and list
mylist = [1, 2, 3, 4]
c = np.array([1, 2, 3, 4])

mylist.append(12)
print(mylist)
# c.append(23) # Array does not support append function
print(c)

mylist = mylist + [5] # it will just add another element
c = c + np.array([5]) # it will add 5 to each element (Its called Broadcasting)

print("Addition using + sign : \n")
print(mylist)
print(c)

# Dot Product 
l1 = [1, 2, 3, 4]
l2 = [2, 4, 6, 8]
a = np.array(l1)
b = np.array(l2)

print("\nDOT PRODUCT METHODS : \n")
dot = 0
print("With method-1 :  ")
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

print("With method-2 :  ")
dot = np.dot(a, b)
print(dot)