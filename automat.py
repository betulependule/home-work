#! /usr/bin/env python3

vstup = 37


def automat(vstup):
    padekoruny = 0
    dvackoruny = 0
    desekoruny = 0
    petkoruny = 0
    dvoukoruny = 0
    koruny = 0
    while vstup > 0:
        if vstup >= 50:
            vstup = vstup - 50
            padekoruny = padekoruny + 1
        elif 50 > vstup >= 20:
            vstup = vstup - 20
            dvackoruny = dvackoruny + 1
        elif 20 > vstup >= 10:
            vstup = vstup - 10
            desekoruny = desekoruny + 1
        elif 10 > vstup >= 5:
            vstup = vstup - 5
            petkoruny = petkoruny + 1
        elif 5 > vstup >= 2:
            vstup = vstup-2
            dvoukoruny = dvoukoruny + 1
        elif 2 > vstup >= 1:
            vstup = vstup - 1
            koruny = koruny + 1
    print("padesatikorun je:", (padekoruny))
    print("dvacetikorun je:", (dvackoruny))
    print("desetikorun je:", (desekoruny))
    print("petikorun je:", (petkoruny))
    print("dvoukorun je:", (dvoukoruny))
    print("korun je:", (koruny))
    return padekoruny, dvackoruny, desekoruny, petkoruny, dvoukoruny, koruny


print(automat(vstup))
