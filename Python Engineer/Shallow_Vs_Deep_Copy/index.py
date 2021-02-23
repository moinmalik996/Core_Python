"""
Shallow_Copy   : One level deep, only refrences of nested child objects
Deep_Copy      : full independent copy

"""

original = [0, 1, 2, 3, 4]
cpy   = original

cpy[0]= -1   # It wll also edit original list

print(original)
print(cpy)


original = [0, 1, 2, 3, 4]

cpy = original.copy()

cpy[0] = -10

print(original)
print(cpy)

