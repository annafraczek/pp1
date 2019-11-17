def suma(tablica):
    suma=0
    print('Tablica: ', end='')
    for i in tablica:
        suma += int(i)
        print('{} '.format(i), end ='')
    print()
    print('Suma: {}'.format(suma))
suma([4,3,7,1,3])