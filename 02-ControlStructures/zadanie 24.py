tab=['Genowefa','Onufry','Celestyna','Alojzy','Pankracy','Teofil']
najdłuższe_imię=0
n=0
for i in range(0,len(tab)):
    if len(tab[i])>n:
        n=len(tab[i])
        najdłuższe_imię=tab[i]
print(f'Najdłuższe imię: {najdłuższe_imię}')