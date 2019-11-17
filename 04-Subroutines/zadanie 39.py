def sprawdzZakres(x,y,liczba):
    if liczba >= x and liczba <= y:
        return print("Liczba znajduje się w zasięgu.")
    else:
        return print("Liczba poza zasięgiem.")


x = int(input("Pierwsza liczba zakresu: "))
y = int(input("Druga liczba zakresu: "))
liczba = int(input("Podaj liczbę: "))

print(sprawdzZakres(x,y,liczba))