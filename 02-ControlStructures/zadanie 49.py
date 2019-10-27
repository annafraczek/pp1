dni = ['P', 'W', 'S', 'C', 'Pt', 'S', 'N']

nrDniaTygodnia = 2
ostatniDzien = 30

print('|', end = ' ')
for dzien in dni:
    print(dzien, ' \t|', end=' ')
print('')

print('      |', end = ' ')
for numer in range(1, ostatniDzien + nrDniaTygodnia + 1):
    if (numer <= nrDniaTygodnia):
        print(' \t|', end=' ')
    else:
        print(numer - nrDniaTygodnia, ' \t|', end=' ')
    if (numer % 7 == 0):
        print('')
        print('|', end="")