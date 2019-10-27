pesel = input("Podaj pesel: ")

pesel_wiek = int(pesel[0:2])
pesel_plec = int(pesel[9])

if pesel_plec%2 == 0:
    płeć = "kobieta"
else:
    płeć = "mężczyzna"

if int(pesel[2]) > 1:
    urodzona_po_2000 = True
else:
    urodzona_po_2000 = False


print('Osoba to: ', płeć, end=', ')
if urodzona_po_2000 == True :
    pesel_wiek = 2000+int(pesel_wiek)
    wiek = 2018 -pesel_wiek
    print(" ma ", wiek, ' lat')
else:
    pesel_wiek = 1900+int(pesel_wiek)
    wiek = 2018 - pesel_wiek
    print("ma", wiek, ' lat')