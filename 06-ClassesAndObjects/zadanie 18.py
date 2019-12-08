import random


class Kostka:

    def rzuc(self):
        rzut = random.randint(1, 6)
        print("wyrzucono:", rzut)
        return rzut


kostka1 = Kostka()
kostka2 = Kostka()
kostka3 = Kostka()

listaKostek = [kostka1, kostka2, kostka3]
listaWynikow = []

for i in range(3):
    proba = listaKostek[i].rzuc()
    listaWynikow.append(proba)

print(sum(listaWynikow))
