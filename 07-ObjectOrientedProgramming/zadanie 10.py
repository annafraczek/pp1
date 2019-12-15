class Point(): 
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
    def __str__(self): 
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y


p1 = Point(4,2)
p2 = Point(7,2)

if p1 == p2:
    print(f'{p1} == {p2}')
    print('Odległość między punktami wynosi 0.')
else:
    from math import sqrt
    d = sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    print(f'{p1} == {p2}')
    print(f'Odległość między punktami wynosi {d}.')