def factorial(n):
    if n < 0 or n % 1 != 0:
        return
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(2))
