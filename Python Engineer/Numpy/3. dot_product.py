# Dot Product is the sum of 


import numpy as np
from numpy.core.getlimits import _discovered_machar


l1 = [1, 2, 3]
l2 = [4, 5, 6]

a = np.array([1, 2, 3])

dot_prod = 0

for i in range(len(l1)):
    dot_prod += l1[i] * l2[i]
print(dot_prod, end="\n")

array_dot = np.dot(l1, l2)
print(array_dot, end="\n")

sum1 = l1 * l2
dot  = (l1 * l2).sum()
print(dot)



