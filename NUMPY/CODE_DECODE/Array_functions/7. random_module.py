"""
Random module is the part of numpy

Popular Methods Include :

rand()
randn()
randf()
randint()


"""

import numpy as np
from numpy.core.fromnumeric import size

print(np.random.rand(1, 5))
print()
print(np.random.randn(2, 3))  # array of 2 rows 3 columns

print()
print(np.random.randint(1, 10, size=(2, 3))) # 1, 10 are range for random numbers
                                             # size is array shape


