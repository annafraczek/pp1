suma_liczb_parzystych=0
suma_liczb_nieparzystych=0
for i in range(1,51):
    if i%2==0:
        suma_liczb_parzystych+=1
    else:
        suma_liczb_nieparzystych+=1
print(f'Suma liczb parzystych: {suma_liczb_parzystych}, suma liczb nieparzystych {suma_liczb_nieparzystych}')