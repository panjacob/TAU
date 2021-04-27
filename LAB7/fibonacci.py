def fib(n):
    if type(n) is not int:
        return None
    elif n < 0:
        return None
    elif n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
