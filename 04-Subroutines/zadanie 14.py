def wystepuje(liczba, tablica):
    if liczba in tablica:
        print('Podana liczba występuje w tablicy.')
    else:
        print('Podana liczba nie występuje w tablicy.')

tablica=[15, 38, 7, 23, 14]
liczba= int(input('Wpisz liczbę: '))
wystepuje(liczba, tablica)