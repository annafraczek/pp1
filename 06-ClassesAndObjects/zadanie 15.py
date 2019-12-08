class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
        self.volume = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self,new_channel_no):
        self.channel = new_channel_no
    def b_volume(self):
        if self.volume<10:
            self.volume+=1
    def s_volume(self):
        if self.volume>0:
            self.volume-=1        
    def show_status(self,tab):
        if self.is_on == True:
            print(f'Telewizor jest włączony. Głośność: {self.volume}. Numer kanału: {self.channel} {tab[self.channel-1]}')
            
        else:
            print('Telewizor jest wyłączony.')
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        for x in range(len(self.channels)):
            print(f'{x+1}. {self.channels[x]}')

tab=['TVP1','TVP2','TVN','POLSAT','TVN7','ABC','TVNTurbo']


tv1 = TV()
tv1.show_status(tab)
tv1.on()
tv1.set_channels(tab)
tv1.set_channel(4)
tv1.b_volume()
tv1.show_status(tab)
tv1.b_volume()
tv1.show_status(tab)
tv1.b_volume()
tv1.show_status(tab)
tv1.b_volume()
tv1.show_status(tab)
tv1.b_volume()
tv1.show_status(tab)
tv1.b_volume()
tv1.show_status(tab)
tv1.s_volume()
tv1.show_status(tab)
tv1.s_volume()
tv1.show_status(tab)
tv1.off()