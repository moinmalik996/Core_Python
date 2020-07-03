def highest_even(my_list):
    evens = []
    for item in my_list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([1, 2, 3, 66, 78, 99, 100, 120, 34, 55]))
