import random

def liczbaLosowa():
    return random.randint(1,50)

print(liczbaLosowa())

liczbaParzysta = 0
liczbaNieparzysta = 0
for i in range(1000):
    a = liczbaLosowa()
    if a%2 == 0:
        liczbaParzysta = liczbaParzysta + 1
    else:
        liczbaNieparzysta = liczbaNieparzysta + 1

procentParz = (liczbaParzysta/1000 * 100)
procentNparz = (liczbaNieparzysta/1000 * 100)

print("Liczby parzyste stanowią: ", '%.2f'%procentParz, '%')
print("Liczby nieparzyste stanowią: ", '%.2f'%procentNparz, '%')