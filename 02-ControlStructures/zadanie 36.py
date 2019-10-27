x = 0
while True:
    if(x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1 and x % 7 == 0):
        break
    x += 1
print("Pierwsza liczba pierwsza spełniajaca warunki to:", x)