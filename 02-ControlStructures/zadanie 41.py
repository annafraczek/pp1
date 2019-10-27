from statistics import mean
ile_liczb = int(input("Ile liczb chcesz podać? "))
liczby = []
for i in range(ile_liczb):
    a = int(input('Podaj liczbę: '))
    liczby.append(a)

print("REZULTAT: ", len(liczby), ", suma:", sum(liczby), ", średnia: ", mean(liczby))