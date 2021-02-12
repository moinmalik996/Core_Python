import numpy as np


a = np.arange(1, 7)  # It will create an array of 6 int elements
b = a
print(b)

print("Shape of Array-b : ", b.shape) # Tells the no of Rows and Columns
b = b.reshape(2, 3)  # Split the straight array into resired rows and columns
print("\nAfter Reshape of Array-b : b.reshape(2, 3)")
print(b)

# NEWAXIS METHOD : It is used to increase the Dimension of the array
print("\nNew dimension added with 1 column : c = a[:, np.newaxis]")
c = a[:, np.newaxis] # It will add dimension with 1 column
print("Array-c Now  :  ", c)
print("Shape of Array-c now  :  ", c.shape)


print("\nNew dimension added with 1 row : c = a[np.newaxis, :]")
c = a[np.newaxis, :] # It will add dimension with 1 row
print("Array-c Now  :  ", c)
print("Shape of Array-c n", c.shape)



