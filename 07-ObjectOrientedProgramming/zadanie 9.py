class Message(): 
    def __init__(self):
        self.message = '' 

    def set_message(self,message):
        message1 = message
        self.message += message1[0].upper() + message1[1:].lower() + ' BYE.'

class SMS(Message):
    def __init__(self,telefon):
        self.telefon = telefon
        super().__init__()
    def send(self):
        print(f'\nWysyłanie SMS...\nDo: {self.telefon}\nTreść: {self.message}')

class Email(Message):
    def __init__(self,odbiorca,temat):
        self.nadawca = 'kowalski@wp.pl'
        self.odbiorca = odbiorca
        self.temat = temat
        super().__init__()
    def send(self):
        print(f'\nWysyłanie E-Maila...\nOd: {self.nadawca}\nDo: {self.odbiorca}\nTemat: {self.temat}\nTreść: {self.message}')

m1 = SMS('345223555')
m1.set_message('Hej')
m1.send()

m2 = Email('nowak@interia.pl','Spotkanie.')
m2.set_message('Spotkanie w tym tygodniu jest odwołane.')
m2.send()