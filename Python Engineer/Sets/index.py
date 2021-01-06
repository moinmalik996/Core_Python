# Sets :  Unordered , Mutable , No Duplicates

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset.add(3)

# for item in myset:
#     print(item)

# print(type(myset))

# evens = {2, 4, 6, 8, 10}
# odds = {1, 3, 5, 7, 9}
# primes = {2, 3, 5, 7}

# unoin =odds.union(evens)
# print(unoin)

# intersection = evens.intersection(odds)
# print(intersection)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)              # Return elements of setA that are not in setB
# diff2 = setA.symmetric_difference(setB)   # Return all the elements that are different from both sets.
# print(diff)
# print(diff2)

# #setA.update(setB)
# # setA.intersection_update(setB)
# setA.difference_update(setB)
# print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))  # is setA a subset of setB
print(setB.issubset(setA))  # Is setB a subset of setA