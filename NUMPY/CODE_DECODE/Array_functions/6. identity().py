# identity()  :  Returns a square matrix containing 1's
#                in the main diagonal and other elements 
#                being zero.

"""
Difference between eye() and identity is that in eye()
function we decide which diagonal will contain 1's.

"""

import numpy as np

print(np.identity(5, dtype=complex))