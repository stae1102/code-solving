def fibonacci(n):
    if n >=2: return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        if n < 0: pass
        return n
print(fibonacci(int(input())))
