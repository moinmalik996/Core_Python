# Decorators : A decorator function is the one who accepts
#              a function as argument, modify it and returns a functon.
# We use @sfunction_name to specify a decorator to be applied on another function

def decor(func_argu):
    def inner():
        print("Hamza Malik")
        func_argu()
        print("Ali Malik")
    return inner()



@decor
def fun():
    print("Moin Malik")
    print("Junaid Malik")
    
    
def enhance(add):
    def inner():
        a = add()
        ad = a + 5
        return ad
    return inner()


@enhance
def add():
    return 10

print(add)




