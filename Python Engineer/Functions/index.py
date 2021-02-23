"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)

"""

def print_name(name):
    print(name)   
print_name('Moin Malik')



def foo(a, b, c):
    print(a, b, c)    
foo(1, 2, 3)
foo(a=23, b=56, c=34)
foo(1, b=2, c=12) 
# foo(11, b=12, 13)  # can't use default value after positional argument



def myfunc(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
myfunc(1, 2, 3, 4, 5, 6, seven=7, eight=8) # 1, 2 = a, b
                                           # 3, 4, 5, 6 are *args
                                           # seven, eight are **kwargs
                                           


