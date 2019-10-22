wiek=int(input('Podaj wiek psa w ludzkich latach: '))

if wiek<3:
    l=wiek*10.5
else:
    l=21+(wiek-2)*4
    
print(f'Wiek psa w psich latach to: {l}')