def fib(n):
    if n>2: 
        return fib(n-2)+fib(n-1)
    elif n==2:
        return fib(1)+1
    elif n==1:
        return 0


x=1
while x<21:
    print(fib(x))
    x+=1