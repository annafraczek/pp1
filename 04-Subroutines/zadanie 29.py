from statistics import mode

tablica = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]

def mediana(tablica):
    tablica = sorted(tablica)
    if len(tablica)%2 != 0:
        indeks = int(len(tablica)/2 + 1)
        mediana = tablica[indeks-1]
        print('Mediana to:', mediana)
        return mediana
    elif len(tablica)%2 == 0:
        indeks = int(len(tablica)/2)
        mediana = (tablica[indeks] + tablica[indeks-1])/2
        print('Mediana to:', mediana)
        return mediana

def dominanta(tablica):
    dominanta = mode(tablica)
    print('Dominanta to:', dominanta)
    return dominanta

mediana(tablica)
dominanta(tablica)