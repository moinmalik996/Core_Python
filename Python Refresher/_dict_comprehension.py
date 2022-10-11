data = [
    (0, 'Bob', 'malik1122'),
    (1, 'Malik', 'malik1122'),
    (2, 'Hamza', 'malik1122'),
    (3, 'Junaid', 'malik1122'),
    (4, 'Saad', 'saad'),
]

user_names = {user[1]:user for user in data}

print(user_names)