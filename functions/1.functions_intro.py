def hello(greeting, name='Moin'):
    return '{},  {}'.format(greeting, name)


def details(*args, **kwargs):
    print(args)
    print(kwargs)


list1 = ['Physics', 'Chemistry']
dict1 = {'name': 'Moin Abbas Malik', 'age': 20}

details(*list1, **dict1)

print(hello('Hi', 'Abbas'))
