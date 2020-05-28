student = {'name': 'Moin Malik', 'age': 20, 'subjects': ['Chemistry', 'Physics']}

print(student['subjects'])

print(student.get('phone', 'Not Found'))

# updating dictionary
student.update({'name': 'John', 'age': 10, 'phone': '555-55555-67'})
print(student)

# deleting from dictionary

age = student.pop('age')
print(student)

# getting all the keys from dictionary
print(student.keys())
# getting all the items from dictionary
print(student.items())  # it prints both keys and values

print("\n")
for key, value in student.items():
    print(key, " :  ", value)
