def multiply(args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
        
    return total


# def sum(*args):
#     total = 0
#     print(args)
#     for arg in args:
#         total += arg
#     return total


def apply(*args, operator):
    if operator == '+':
        print('sum')
        return sum(args)
    elif operator == '*':
        return multiply(args)
    else:
        return "No valid operator provided to apply()"
    

print(apply(1, 2, 3, 4, 5, operator='*'))