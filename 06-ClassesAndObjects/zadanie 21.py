class Statystyka:
    listaLiczb = []

    def dodaj_liczbe(self):
        liczba = int(input("Podaj liczbę"))
        self.listaLiczb.append(liczba)


    def wyswietl_liczby(self):
        print("Liczby: ", end = " ")
        for i in self.listaLiczb:
            print(i, end=" ")
        print("")

    def najwieksza(self):
        print("najwieksza wartosc z listy to:", max(self.listaLiczb))

    def najmnijesza(self):
        print("najmniejsza wartosc z listy to:", min(self.listaLiczb))

    def srednia(self):
        wynik = 0
        for i in self.listaLiczb:
            wynik += i
        wynik = wynik/len(self.listaLiczb)
        print("średnia to: ", wynik)

    def mediana(self):
        import statistics
        mediana = statistics.median(self.listaLiczb)
        print("Mediana wynosi:", mediana)

    def wszystko(self):
        self.wyswietl_liczby()
        self.najwieksza()
        self.najmnijesza()
        self.srednia()
        self.mediana()

st = Statystyka()
st.dodaj_liczbe()
st.dodaj_liczbe()
st.dodaj_liczbe()

st.wyswietl_liczby()
st.najmnijesza()
st.najwieksza()
st.srednia()
st.mediana()
st.wszystko()