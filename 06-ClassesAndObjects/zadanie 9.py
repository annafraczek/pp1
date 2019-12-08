class University():
    # konstruktor obiektu(metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.name = 'UEK' # zachowania obiektu (metody)
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
        
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,new_fullname):
        self.fullname = new_fullname
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name    
        
uek = University()

uek.print_name()
uek.print_fullname()
uek.set_name('AGH')
uek.set_fullname('Akademia Górniczo Hutnicza')
uek.print_name()
uek.print_fullname()