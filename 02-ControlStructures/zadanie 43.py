lista = []
a = int(input("Podaj liczbę 1: "))
lista.append(a)
b = int(input("Podaj liczbę 2: "))
lista.append(b)
c = int(input("Podaj liczbę 3: "))
lista.append(c)

lista.sort()

print('Liczby w kolejności rosnącej:', lista[0], lista[1], lista[2])