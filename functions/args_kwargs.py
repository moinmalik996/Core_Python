#  *args   **kwargs

def super_func(*args):
    print(args)
    return sum(args)


def my_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1,2,3,4,5))
print(my_func(1,2,3,4,5, num1=20, num2=30))


# Rule is : parameterss, *args, default parameters, **kwargs

