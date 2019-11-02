import re
liczby = []
f = open('C:/Users/Anna/Desktop/pp1/03-FileHandling/numbers.txt', 'r')
liczby = [line.rstrip('\n') for line in f]
liczby = [int(i) for i in liczby]

liczby = sorted(liczby)

for i in range(len(liczby)):
    print(liczby[i], end = ' ')