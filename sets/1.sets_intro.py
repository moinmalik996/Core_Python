# check whether a value is in the group or not
# they don't care about order/index

cs_courses = {"Physics", "Chemistry", "Mathematics", "IT", "CS"}
art_courses = {"Urdu", "English", "Islamic", "Mathematics", "Physics"}

print('IT' in cs_courses)

print(cs_courses.intersection(art_courses))  # Common Courses
print(cs_courses.difference(art_courses))  # Different Courses
print(cs_courses.union(art_courses))  # Join Two Sets without Duplicating
