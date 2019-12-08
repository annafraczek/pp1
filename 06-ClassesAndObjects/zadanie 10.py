class Telewizor:
    is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        if not self.is_on:
            print("Telewizor jest wyłączony")
        else:
            print("Telewizor jest włączony")


t1 = Telewizor()
t1.status()
t1.turn_on()
t1.status()
t1.turn_off()
t1.status()
