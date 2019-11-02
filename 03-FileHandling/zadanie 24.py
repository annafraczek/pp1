import csv
lista = [['imie', 'nazwisko', 'email'],['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
with open('csv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
file.close()