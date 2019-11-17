imiona=['Janek','Ania','Wojtek','Zosia']
def jestImie(x,y):
    if x in imiona:
        return 1
    else:
        return 0
    

imie=input('Podaj imię: ')
if jestImie(imie,imiona)==1:
    print('Imię znajduje się w wykazie.')
else:
    print('Imienia nie ma w wykazie.')