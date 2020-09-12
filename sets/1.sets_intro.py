# Unordered, Mutable, No Duplicates



cs_courses = {"Physics", "Chemistry", "Mathematics", "IT", "CS"}
art_courses = {"Urdu", "English", "Islamic", "Mathematics", "Physics"}



print('\n')
print('IT' in cs_courses)

print('\n')
print(cs_courses.intersection(art_courses))  # Common Courses
print(cs_courses.difference(art_courses))  # Different Courses
print(cs_courses.union(art_courses))  # Join Two Sets without Duplicating

#to_check_which_characters_are_in_your_string
my_string = "Moin Malik"
myset = set(my_string)
print('\n', myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

print('\n', myset)
print('')
for x in myset:
    print('\n', x)
    
    
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}

diff = setA.difference(setB) #Elements of Set A that are not in Set B
print()
print(diff)

diff = setB.difference(setA) #Elements of Set B that are not in Set A
print()
print(diff)

diff = setA.symmetric_difference(setB)
print()
print(diff)

issubset = setA.issubset(setB)   #  is set A is subset of Set B
print("\nIs Set-A subset of Set-B  :  ", issubset)


