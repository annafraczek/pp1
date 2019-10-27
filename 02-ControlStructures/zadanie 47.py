kwota = int(input("Podaj kwotę: "))

moneta5 = int(kwota/5)
reszta1 = int(kwota - moneta5*5)

moneta2 = int(reszta1/2)
reszta2 = int(kwota - (moneta5*5) - (moneta2*2) )

moneta1 = int(reszta2/1)

print("Kwota do wydania w monetach: ", kwota)
print("liczba monet 5zł: ", moneta5)
print("liczba monet 2zł: ", moneta2)
print("liczba monet 1zł: ", moneta1)