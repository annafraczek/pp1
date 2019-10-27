a = 50

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = list(fib(a))

for x in range(len(fib)):
    print(fib[x], end=",")