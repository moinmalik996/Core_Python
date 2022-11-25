def fibonaci(n):
    if n == 0:
        return 0
    else:
        return fibonaci(n-1)

print(fibonaci(10))