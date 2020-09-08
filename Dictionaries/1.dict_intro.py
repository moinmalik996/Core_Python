# Dictionaries :  Key-Value Pairs, Unordered , Mutable

mydict = {"name": "Moin", "Age": 23, "City": "Sialkot"}

print("\n", mydict)

mydict2 = dict(name="Moin", age=23, City="Sialkot")

print("\n", mydict2)

# Printing Values
value = mydict["Age"]
print("\n", value)

#adding key-Value pairs
mydict["email"] = "moin.malik996@gmail.com"
print("\n", mydict)

#deleting items from dict
mydict.popitem()
print("\n", mydict)

#Printing the keys of dict
for key in mydict.keys():
    print("\n", key)
    
#Printing the values of dict
for values in mydict.values():
    print("\n", values)

#Printing the keys,values of dict at same time
# for keys, values in mydict:
#     print(keys, "  :  ", values)