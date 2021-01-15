# lambda arguments: expresion
# filter(funx, seq)
# reduce(func, seq)

from functools import reduce


# both add1 and add2 act as same 
add1 = lambda x: x + 1

def add2(x):
    return x + 1

print(add1(10))
print(add2(10))

mult = lambda x, y: x * y
print(mult(2, 3))


points2d = [(1, 2), (-1, 10), (12, -19), (3, 6), (-10, -2)]
points2d_sorted_x = sorted(points2d, key=lambda x: x[0])
points2d_sorted_y = sorted(points2d, key=lambda y: y[1])

print(points2d)
print("\n\nSorted by 1st element of each index.")
print(points2d_sorted_x)
print("\n\nSorted by 2nd element of each index.")
print(points2d_sorted_y)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2 , a)  # It will multiply list a elements with 2
print(list(b))

# LIST COMPREHENSION 
list_a = [1, 2, 3, 4, 5, 6]
list_b = [x * 2 for x in list_a]
print("\n\nLIST COMPREHENSION")
print(list_a)
print(list_b)

# FILTER FUNCTION
print("\n\nFILTER FUNCTION\n")
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_a)
list_b = filter(lambda x: x % 2 == 0, list_a) # Filter the even numbers
print(list(list_b))

# REDUCE FUNCTION
list_a = [1, 2, 3, 4]
reduc = reduce(lambda x, y: x * y, list_a)
print(reduc)