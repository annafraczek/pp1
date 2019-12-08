class RachunekBankowy:
    saldo = 0
    def __init__(self, numer):
        if len(str(numer)) != 26:
            print('niepoprawny numer konta')
        else:
            self.numer = str(numer)

    def informacje(self):
        print("Numer Konta:",self.numer[0:2],self.numer[2:6], self.numer[6:10], self.numer[10:14], self.numer[14:18], self.numer[18:22], self.numer[22:26])
        print("Saldo konta wynosi:", self.saldo)

    def wplac(self, kwota):
        self.saldo += kwota

    def wyplac(self, kwota):
        if self.saldo - kwota < 0:
            print("Nie masz wystarcząco środków na koncie.")
        else:
            self.saldo -= kwota

rachunek = RachunekBankowy(12345655559090111100007722)
rachunek.informacje()
rachunek.wplac(25.30)
rachunek.informacje()
rachunek.wyplac(31.79)
rachunek.informacje()
rachunek.wyplac(14)
rachunek.informacje()