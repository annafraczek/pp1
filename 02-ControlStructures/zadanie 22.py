tablica=[15,8,31,47,2,19]
suma=0
x=0
for i in range(0,len(tablica)):
    if tablica[i]%2!=0:
        suma+=tablica[i]
        x+=1
print(f'Średnia arytmetyczna: {suma/x}')