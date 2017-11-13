#! /usr/bin/env python3

import random
kolo = 0
vitezstvi = 0
prohry = 0


def kamen_nuzky_papir(kolo, vitezstvi, prohry):
    while kolo <= 2:
        hrac = input("Jaka je tva volba? Kamen, nuzky nebo papir?")
        if hrac != "kamen" and hrac != "nuzky" and hrac != "papir":
            print("Preklepy nema Python rad. Uz s tebou nehraju.")
            break
        protihrac = random.randrange(1, 4)
        if protihrac == 1:
            protihrac = "kamen"
        elif protihrac == 2:
            protihrac = "nuzky"
        elif protihrac == 3:
            protihrac = "papir"
        print("Pocitac dava {}".format(protihrac))
        if hrac == "kamen" and protihrac == "nuzky":
            print("Toto kolo vyhravate!")
            vitezstvi = vitezstvi + 1
            kolo = kolo + 1
        elif hrac == "nuzky" and protihrac == "papir":
            print("Toto kolo vyhravate!")
            vitezstvi = vitezstvi + 1
            kolo = kolo + 1
        elif hrac == "papir" and protihrac == "kamen":
            print("Toto kolo vyhravate!")
            vitezstvi = vitezstvi + 1
            kolo = kolo + 1
        elif hrac == protihrac:
            print("Remiza! Kolo se opakuje!")
        else:
            print("Toto kolo vyhrava pocitac!")
            prohry = prohry + 1
            kolo = kolo + 1
    if vitezstvi > prohry:
        print("Gratutujeme! Zvitezili jste nad pocitacem!")
    elif vitezstvi < prohry:
        print("Smula! Prohrali jste proti pocitaci!")


kamen_nuzky_papir(kolo, vitezstvi, prohry)
