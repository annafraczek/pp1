tekst='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def ile(a,tekst):
    l=0
    for x in tekst.lower():
        if x==a: l+=1
    return l
a=input('Podaj samogłoskę: ')
print(f'Samogłoska {a} występuje w tekście {ile(a,tekst)} razy.')