class Termometr:
    termometr_ison = False
    temperatura = 0

    def wlaczTermometr(self):
        self.termometr_ison = True
        self.temperatura = 36.6

    def wylaczTermometr(self):
        self.termometr_ison = False
        self.temperatura = 0

    def zmierzTemperature(self):
        if self.termometr_ison == True:
            import random
            self.temperatura = random.uniform(34, 42)
            if self.temperatura > 37 and self.temperatura < 41:
                print('%.1f'% self.temperatura, " - Groączka!")
            elif self.temperatura > 41:
                print('%.1f'%self.temperatura, " - Gorączka! Zagrożenie życia!!!")
            else:
                print('%.1f'%self.temperatura)

        else:
            print("termometr wyłączony")

