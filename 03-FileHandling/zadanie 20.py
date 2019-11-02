import re
liczby = []

wczytajPlik = 'C:/Users/Anna/Desktop/pp1/03-FileHandling/numbers.txt'
zapiszDo = 'C:/Users/Anna/Desktop/pp1/03-FileHandling/evennumbers.txt'
f = open(wczytajPlik, 'r')
liczby = [line.rstrip('\n') for line in f]
liczby = [int(i) for i in liczby]

liczby = sorted(liczby)

parzyste = []
for i in range(len(liczby)):
    if liczby[i]%2==0:
        parzyste.append(liczby[i])

with open(zapiszDo, 'w') as file:
    for lista in parzyste:
        file.write('%s\n' % lista)