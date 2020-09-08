mylist  = ["Moin", "Malik", "Abbas", "Junaid", "Hamza", "Ali", "Saad"]

list_slice = mylist[0:5]

"""

if we dont specify start index eg [:5]
              it will start from 0 index
if we dont specify last index eg  [5:]
              if will end at  last index
"""

list_slice = mylist [:3]

print()
print("Between 1st and 3rd element" , list_slice)

list_slice = mylist[5:]

print()
print("Between 5th and last element", list_slice)

mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_slice = mylist2[::3]   #step index at last

print()
print(list_slice)

list_slice = mylist2[::-1]

print()
print(list_slice)