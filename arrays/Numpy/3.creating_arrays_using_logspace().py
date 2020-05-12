"""
logspace() function is used to create an array with evenly
spaced numbers logarithmically .

logspace(start, stop, num, endpoint=True, base = 10.0, dtype = None, axis = 0)

start = base ^ start
stop = base ^ stop
num = no. of pieces to divide in
base = the base of the log space

e.g:
        logspace(1, 3, 5, base = 10)

"""

from numpy import *

stu_rol = logspace(1, 3, 10, base=10, dtype=int)

for el in stu_rol:
    print(el)