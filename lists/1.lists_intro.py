my_list = [12, "Moin Malik", 85, "Ali", 34, 56.8]
my_list_2 = ["Malik", "Moin", "Abbas"]

my_numbers = [12, 11.5, 5, 90, -11, -12.5]

list_length = len(my_list)

print(my_list)
print(list_length)
print(my_list[0:3])

my_list.extend(my_list_2)
print(my_list)

my_list.reverse()
print(my_list)

sorted_num = sorted(my_numbers)

print(sorted_num)  # Sort The Numbers
print(min(my_numbers))  # print min Value
print(max(my_numbers))  # print max Value


