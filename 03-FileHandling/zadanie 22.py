import re
with open('C:/Users/Anna/Desktop/pp1/03-FileHandling/students.txt','r') as file:
    for x in file:
        y=re.split(',',x)
        if y[2]!='age':
            if int(y[2])<30:
                print('{}  {}  {}'.format(y[0],y[1],y[4]))