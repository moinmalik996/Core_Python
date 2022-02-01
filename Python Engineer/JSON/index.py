import json
from os import name


# person = { "name": "Moin", "age": 65, "City": "New York", "hasChildren": True, "titles": ["Malik", "Chaudry", "Rana"] }

# personJSON = json.dumps(person, indent=4, sort_keys=True) # DUMPS FOR STRING
# # print(personJSON)

# file_path = r"Python Engineer\JSON\example.json"


# # writing into file
# with open(file_path, 'w') as myfile:
#     json.dump(person, myfile, indent=4)  # DUMP FOR NOT_STRING

# # reading from file
# with open(file_path, 'r') as myfile:
#     person = json.load(myfile)
#     print(person)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Moin", 23)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        return TypeError("Object of type USER is not JSON serializable.")


from json import JSONEncoder

userJSON = json.dumps(user, default=encode_user)
print(userJSON)
