def liczby(tab):
    for x in range(len(tab)):
        if tab.count(tab[x])>1:
            a=tab[x]
            for i in range(len(tab)):
                if tab[i]==a:
                    tab[i]=None
    for x in range(tab.count(None)):
        tab.remove(None)
    return tab
tab=[1,4,1,5,5,2,7,1,6,1]
print(liczby(tab))