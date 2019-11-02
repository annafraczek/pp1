plikDoOdczytu = 'C:/Users/Anna/Desktop/pp1/03-FileHandling/numbersinrows.txt'

import re

with open(plikDoOdczytu) as file:
    zawartość = file.readlines()
    wynik = []
    for line in zawartość:
        listaTymczasowa = line.split(',')
        for x in listaTymczasowa:
            wynik.append(re.findall(r'\d+', x)[0])
        wynik =[int(i) for i in wynik]

print('Liczb jest:', len(wynik))
print('Suma tych liczb to:', sum(wynik))