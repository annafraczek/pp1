with open('C:/Users/Anna/Desktop/pp1/03-FileHandling/shoppinglist.txt','a') as file:
    produkt=input('Nazwa produktu: ')
    file.write(produkt+'\n')