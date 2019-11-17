def sumaCyfr(numer):
    if numer == 0:
        return 0
    else:
        return (numer%10) + sumaCyfr(numer//10)

print(sumaCyfr(1233))

def funkcjaSprawdzajaca(liczba):
    a = sumaCyfr(liczba)
    liczba = str(liczba)
    dodaj = []
    for i in range(len(liczba)):
        dodaj.append(int(liczba[i]))
    b = sum(dodaj)
    print(a == b)

funkcjaSprawdzajaca(12)