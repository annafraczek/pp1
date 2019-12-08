class Telewizor:
    __is_on = False
    __channel = 1

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def status(self):
        if not self.__is_on:
            print("Telewizor jest wyłączony")
        else:
            print("Telewizor jest włączony. Aktualny kanał to:", self.__channel, ".")

    def set_channel(self, channel):

        if self.__is_on == True:
            self.__channel = channel
        else:
            print("Nie można zmienić kanału jeśli TV jest wyłączony")


t1 = Telewizor()
t1.status()
t1.turn_on()
t1.status()
t1.set_channel(5)
t1.status()
t1.turn_off()
t1.status()

