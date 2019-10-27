limit_predkosci = int(input("Limit prędkości: "))
predkosc = int(input("Prędkość: "))


if (predkosc < limit_predkosci + 10) and (predkosc > limit_predkosci) :
    mandat = (predkosc - limit_predkosci) * 5
    print("Mandat (zł): ", mandat)
elif (predkosc > limit_predkosci) + 10 and (predkosc > limit_predkosci) :
    mandat = predkosc - limit_predkosci
    mandat = (mandat - 10) * 15
    mandat2 = 5*10
    print("Mandat (zł): ", mandat+ mandat2)