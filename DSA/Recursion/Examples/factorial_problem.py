def factorial(n):

    if n == 0:
        # print('n == 0')
        return 1
    else:
        print('N = ', n)
        # print ('n * factorial(n - 1)', n * factorial(n - 1))
        return n * factorial(n - 1)


print(factorial(4))