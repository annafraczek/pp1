znak = '*'
def prostokat(szerokość, długość):
    print(szerokość * '*')
    for i in range(długość-2):
        print('*' + (szerokość-2)*' '+'*')
    print(szerokość * '*')

prostokat(15,4)