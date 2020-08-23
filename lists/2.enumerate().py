# Print value with index
#!/usr/bin/python

my_list = ["Mon ", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for index, value in enumerate(my_list, start=1):
    print(index, value)
print('\n')

for i, char in enumerate("Moin Malik"):
    print(i, char)
