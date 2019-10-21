import random
wylosowana_liczba = random.randrange(1, 6)
zgadywana_liczba = int(input("Wybierz liczbę "))
print(wylosowana_liczba)

if zgadywana_liczba == wylosowana_liczba:
    print("Brawo! Zgadłeś!")
else:
    print("Nie zgadłeś!")