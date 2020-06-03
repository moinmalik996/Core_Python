x = "global x"


def outer():
    x = "global x"

    def inner():
        nonlocal x
        x = "local x"
        print(x)

    inner()
    print(x)


outer()
print(x)

# def myfunction():
#     global x
#     y = "local y"
#     x = "local x"
#     print(y)
#     print(x)
#
#
# myfunction()
# print(x)
