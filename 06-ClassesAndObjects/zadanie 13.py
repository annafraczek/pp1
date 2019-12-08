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
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        for x in range(len(self.channels)):
            print(f'{x+1}. {self.channels[x]}')

tab=['TVP1','TVP2','TVN','POLSAT','TVN7']


tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.set_channels(tab)
tv1.show_channels()
tv1.show_status()
tv1.off()