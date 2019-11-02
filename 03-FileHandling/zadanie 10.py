suma_liczb=0
with open('C:/Users/Anna/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for x in file:
        suma_liczb+=int(x)
print(suma_liczb)