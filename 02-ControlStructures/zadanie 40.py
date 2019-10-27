import random

lista_rzutow = []
for i in range(100):
    a = random.randint(1,6)
    lista_rzutow.append(a)

print('liczba 1: ',lista_rzutow.count(1))
print('liczba 2: ',lista_rzutow.count(2))
print('liczba 3: ',lista_rzutow.count(3))
print('liczba 4: ',lista_rzutow.count(4))
print('liczba 5: ',lista_rzutow.count(5))
print('liczba 6: ',lista_rzutow.count(6))