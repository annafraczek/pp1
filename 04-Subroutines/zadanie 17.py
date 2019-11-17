def rzucKostka():
    import random
    x=random.randrange(1,7)
    return x
a=rzucKostka()
b=rzucKostka()
c=rzucKostka()

print(f'Wyrzucone oczka: {a} {b} {c}')
print(f'Suma oczek: {a+b+c}')