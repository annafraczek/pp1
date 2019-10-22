a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))

p=int((1/2)*(a+b+c))

pole=p*(p-a)*(p-b)*(p-c)**(1/2)

print(f'Pole: {pole}')