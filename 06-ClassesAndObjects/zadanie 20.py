class Lot:
    wysokosc = 0
    w_powietrzu = False

    def __init__(self, numerLotu):
        self.numerLotu = numerLotu

    def start(self, wysokosc):
        if wysokosc > 2000 & wysokosc < 1000:
            print("wysokosc nie miesci sie w zakresie 2000-1000m. Lot się nie rozpocznie")
        else:
            print("Samolot wystartował. Aktualna wysokość to:", wysokosc)
            self.wysokosc = wysokosc
            self.w_powietrzu = True

    def zmniejszWysokosc(self, metry):
        if self.w_powietrzu == True:
            if  metry > 300:
                print("Obnizono lot")
                self.wysokosc = metry
            else:
                print("Nie można obnizyc lotu ponizej 300m!")
        else:
            print("Samolot jest uziemiony. Nie możesz zmienić wysokości.")

    def zwiekszWysokosc(self, metry):
        if self.w_powietrzu == True:
            if metry < 11000:
                print("Zwiększenie wysokości")
                self.wysokosc = metry
            else:
                print("Nie można zwiększyć wyskości. Wyskość docelowa ponad poziomiem 11000m")
        else:
            print("Samolot jest uziemiony. Nie możesz zmienić wysokości.")

    def ladowanie(self):
        if self.w_powietrzu == True:
            if self.wysokosc > 500:
                print("nie możesz wylądować. Obniż lot")
            else:
                print("wylądowano.")
                self.wysokosc = 0
                self.w_powietrzu = False

    def status(self):
        print("Tu ", self.numerLotu, "moja wysokość lotu to", self.wysokosc, "m")


samolot = Lot('LOT881')
samolot.start(1500)
samolot.status()
samolot.zwiekszWysokosc(8900)
samolot.status()
samolot.zmniejszWysokosc(200)
samolot.status()
samolot.ladowanie()
samolot.status()