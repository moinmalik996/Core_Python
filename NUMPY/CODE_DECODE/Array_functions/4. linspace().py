#  linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

import numpy as np

# help(np.linspace)

arr0 = np.linspace(1, 100, num=5, endpoint=False, retstep=True, dtype='int')  # num : it will break the array in num elements with evenly spaced


print(arr0)