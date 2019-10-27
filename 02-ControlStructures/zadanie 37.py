from statistics import median


liczba1 = int(input("Podaj liczbę: "))
liczba2 = int(input("Podaj drugą liczbą: "))
liczba3 = int(input("Podaj trzecią liczbę: "))
lista_liczb = [liczba1, liczba2, liczba3]


print('Pierwsza liczba to: ', liczba1)
print('Druga liczba to: ', liczba2)
print('Trzecia liczba to: ', liczba3)
print('Mediana wynosi: ', median(lista_liczb))