def podatek(x):
    if x<=5000:
        return 0.17*x
    else:
        a=x-5000
        return 0.17*5000+0.32*a

dochod=int(input('Podaj dochód: '))
print(f'Podatek należny: {round(podatek(dochod),2)} zł')