class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def wyswietl(self):
        print(self.licznik, end="")
        print("/", end="")
        print(self.mianownik, end="")
        print("")

    def uporszczenie(self):
        y = self.licznik
        x = self.mianownik
        while (y):
            x, y = y, x % y

        if x == 1:
            print("nie da się uprościć")

        if x > 1:
            self.licznik = int(self.licznik/x)
            self.mianownik = int(self.mianownik/x)



ulamek = Ulamek(1,2)
ulamek.wyswietl()
ulamek.uporszczenie()
ulamek.wyswietl()

ulamek=Ulamek(12,21)
ulamek.wyswietl()
ulamek.uporszczenie()
ulamek.wyswietl()
