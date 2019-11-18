import math
x=3.5
y=4

sqrtX=math.sqrt(x)
print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')

powX=math.pow(x,y)
print(f'{x} do potęgi {y} wynosi {powX}')

pierw=math.pow(x,1/y)
print(f'Pierwiastek stopnia {y} z {x} wynosi {pierw}')

from math import pi
pole_koła=math.pow(y,2)*pi
print(f'Pole koła o promieniu {y} wynosi {pole_koła}')

silnia=math.factorial(y)
print(f'Silnia {y} wynosi {silnia}')
