n = 25

for liczba in range(n + 1):
    if liczba > 1:
        for n in range(2, liczba):
            if (liczba % n) == 0:
                break
        else:
            print(liczba)