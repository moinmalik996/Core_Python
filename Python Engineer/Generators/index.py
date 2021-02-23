# Generators are Memory Efficient 

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3
    
    
# g = mygenerator()

# print(sorted(g))
# print(sum(g))

# def countdown(num):
#     print("starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)

# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

# This example will clearly define the memory effeciancy of Generators

import sys

def sum_list(n):
    numberes = []  # we store the items in this list which takesalot of memory
    counter = 0
    while counter <= n:
        numberes.append(counter)
        counter += 1
    return numberes

def sum_list_gen(n):
    counter = 0
    while counter <= n:
        yield counter
        counter += 1

print(sum(sum_list(10)))
print(sum(sum_list_gen(10)))

print("\nRespective Sizes\n")

print(sys.getsizeof(sum_list(1000)))
print(sys.getsizeof(sum_list_gen(1000)))