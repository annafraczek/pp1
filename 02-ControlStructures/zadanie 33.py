table=['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
number = input("Podaj jakąś liczbę: ")

for x in number:
    print(table[int(x)], end=' ')