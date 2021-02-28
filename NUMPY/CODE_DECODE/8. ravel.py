import numpy as np


arr0 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

ravel = np.ravel(arr0, order="F")  # Faster than flatten()

print(ravel)