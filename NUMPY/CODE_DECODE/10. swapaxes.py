import numpy as np

arr0 = np.arange(1, 25).reshape(2, 3, 4)

print(arr0)

print()

print(np.swapaxes(arr0, 0, 2))