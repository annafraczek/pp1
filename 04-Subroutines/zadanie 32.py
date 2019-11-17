def transpozycja(macierz):
    new=[]
    x=0
    y=0
    while y<len(macierz[x]):
        temp=[]
        for x in range(0,len(macierz)):
            temp.append(macierz[x][y])
        y+=1
        new.append(temp)
     
    return new

def wyswietl_macierz(macierz):    
    for x in macierz:
        for y in x:
            print(y,end=' ')
        print()
   
macierz=[[1,2,0],[0,0,3],[5,1,1]]
print(f'Macierz początkowa: ',end='\n\n')
wyswietl_macierz(macierz)
print(f'\nMacierz przetransponowana: ',end='\n\n')
wyswietl_macierz(transpozycja(macierz))