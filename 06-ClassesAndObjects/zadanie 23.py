class Kontakt:

    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon

class ListaKontaktow:
    listaKontaktow = []

    def dodajKontakt(self, nazwa, email, telefon):
        kontakt = Kontakt(nazwa, email, telefon)
        self.listaKontaktow.append(kontakt)

    def wyswietlKontakty(self):
        print("LISTA KONTAKTÓW:")
        for i in self.listaKontaktow:
            print(i.nazwa, "  ", i.email, "  ", i.telefon)

lista = ListaKontaktow()

lista.dodajKontakt("Kowalski Jan", "jank@onet.pl", "555234000")
lista.dodajKontakt("Borek Patrycja", "bp@o2.pl", "232000199")
lista.dodajKontakt("Maj Piotr", "maj@google.pl", "222999100")
lista.dodajKontakt("Adamczyk Anna", "ada@poczta.pl", "100200300")

lista.wyswietlKontakty()
