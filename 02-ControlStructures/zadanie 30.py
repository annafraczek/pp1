pin = 9989
próba = 3

while próba != 0:
    wpis = int(input("Podaj pin: "))
    if wpis == pin:
        print("Pin poprawny. Zalogowałeś się!")
        break
    else:
        próba = próba-1
        if próba == 0:
            print("Twoje konto zostało zablokowane!")
            break
        else:
            print("Podałeś złą wartość ! Zostało Ci", próba, " prób")

