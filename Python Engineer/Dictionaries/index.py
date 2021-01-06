# Dictionaries : Key-Value Pair, Mutable, Unordered

name = "name"
age = "Age"
Subject = "Subject"
email = "Email"
username = "username"

mydict = {name : "Moin Malik", age : 23, Subject : "English"}

mydict_cpy = mydict.copy()

mydict_cpy[email] = "moin.malik996@gmail.com"
print(mydict)
print(mydict_cpy)

mydict_2 = dict(name="Hamza", Age=45, Subject="Commerce")

mydict.update(mydict_2)

print(mydict)

# print(mydict)
# print(mydict[name])

# for keys in mydict.values():
#     print(keys)

# mydict[email] = "moin.malik996@gmail.com"

# print(mydict)

# mydict.pop(Subject)

# print(mydict)

# mydict.popitem()  # removes the lest item of Dictionary

# print(mydict)

# if "username" in mydict:
#     print(mydict[username])
    
# try:
#     print(mydict[username])
# except:
#     print("Not Found")