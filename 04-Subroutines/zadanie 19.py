def suma(N):
    if N>0:
        return N + suma(N-1)
    else:
        return 0
print('Suma liczb naturalnych z przedziału <1,N>')
x=int(input('Podaj N: '))
print(f'Suma liczb naturalnych z przedziału <1,{x}> wynosi: {suma(x)}')