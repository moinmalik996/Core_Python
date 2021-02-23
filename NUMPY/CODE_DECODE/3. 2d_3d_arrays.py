import numpy as np

mylist1 = [1, 2, 3, 4, 5]
mylist2 = [6, 7, 8, 9, 10]

mylist3 = [mylist1, mylist2]  # nested list

arr = np.array(mylist3)

print(arr)

arr = np.array([
    [
        [1, 2],
        [1, 2]
    ],
    [
        [9, 8],
        [9, 8]
    ]
])

l1 = [1, 2]
l2 = [3, 4]
l3 = [5, 6]
l4 = [7, 8]
p1 = [l1, l2]
p2 = [l3, l4]
p = [p1, p2]

print("\n\n", arr)

arr = np.array(p)
print("\n\n", arr)