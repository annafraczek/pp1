class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
        
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self,new_channel_no):
        self.channel = new_channel_no
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest włączony. Numer kanału: {self.channel}')
            
        else:
            print('Telewizor jest wyłączony.')
    


tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.off()
tv1.show_status()