class Music:
    def __init__(self,wykonawca,tytuł,album,rok):
        self.wykonawca=wykonawca
        self.tytuł=tytuł
        self.album=album
        self.rok=rok
    def __str__(self):
        return'\nWykonawca: '+' '+f'{self.wykonawca}'+'\nUtwór: '+' '*5 + f'{self.tytuł}'+'\nAlbum: '+' '*5 + f'{self.album}'+'\nRok: '+' '*7 + f'{self.rok}'
    
muzyka=Music('Dawid Podsiadło','Nie ma fal','Małomiasteczkowy','2018')
print(muzyka)
