x=int(input('Wprowadź pierwszą liczbę: '))
y=int(input('Wprowadź drugą liczbę: '))

if x>y:
    print(f'Większa liczba to {x}')
elif x<y:
    print(f'Większa liczba to {y}')
else:
    print('Liczby są równe')