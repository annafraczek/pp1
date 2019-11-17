def potega(x,n):
    if n>0:
        return x*potega(x,n-1)
    else:
        return 1
a=int(input('Podstawa potęgi: '))
b=int(input('Wykładnik potęgi: '))
print(f'{a} do potęgi {b} wynosi {potega(a,b)}')
print(f'5 do potęgi 3 wynosi {potega(5,3)}')