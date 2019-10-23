for i in range(1,31):
    if i%3==0 and i%5==0:
        print(f'BINGO')
    elif i%3==0:
        print(f'THREE')
    elif i%5==0:
        print(f'FIVE')
    else:
        print(i)