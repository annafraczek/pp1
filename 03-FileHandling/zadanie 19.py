ścieżkaDoPliku='C:/Users/Anna/Desktop/pp1/03-FileHandling/universities.txt'
f = open(ścieżkaDoPliku, 'r',encoding= 'utf-8')
uniwersytety = lines = f.read().split('\n')

posortowane=sorted(uniwersytety)

with open(ścieżkaDoPliku, 'w') as file:
    for lista in posortowane:
        file.write('%s\n' % lista)