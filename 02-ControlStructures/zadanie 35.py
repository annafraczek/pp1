import math

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)

print('Wyniki to {0} i {1}'.format(sol1,sol2))