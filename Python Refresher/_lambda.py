def double(x):
    return x * 2


_list = [1, 2, 3, 4, 5, 6, 7, 8]

comp = [double(x) for x in _list]

print(comp)

comp = list(map(double, _list))

print(comp)