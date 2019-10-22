x=str(input("x= "))
y=str(input("y= "))

if x[0]=='0' and y[0]=='0':
    print(f'P({x},{y}) znajduje się w początku układu współrzędnych')
elif x[0]=='0':
    print(f'P({x},{y}) znajduje się na osi y')
elif y[0]=='0':
    print(f'P({x},{y}) znajduje się na osi x')
elif x[0]!='-' and y[0]!='-':
    print(f'P({x},{y}) znajduje się w I ćwiartce')
elif x[0]=='-' and y[0]!='-':
    print(f'P({x},{y}) znajduje się w II ćwiartce')
elif x[0]=='-' and y[0]=='-':
    print(f'P({x},{y}) znajduje się w III ćwiartce')
elif x[0]!='-' and y[0]=='-':
    print(f'P({x},{y}) znajduje się w IV ćwiartce')