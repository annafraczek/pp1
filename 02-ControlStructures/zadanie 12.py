x=str(input('Wpisz pierwszą liczbę: '))
y=str(input('Wpisz drugą liczbę: '))

if x[0]=='-' or y[0]=='-':
    print('Co najmniej jedna liczba jest ujemna')
else:
    print('Obie liczby są dodatnie')