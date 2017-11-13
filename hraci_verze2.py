#! /usr/bin/env python3

import random
kolo = 1


def hraci(kolo):
    vysledky_1 = []
    vysledky_2 = []
    vysledky_3 = []
    vysledky_4 = []
    hody = []
    vyherci = []
    skore = []
    hrac1 = 0
    hrac2 = 0
    hrac3 = 0
    hrac4 = 0
    while kolo <= 5:
        a = random.randrange(1, 7)
        vysledky_1.append(a)
        hody.append(a)
        print("Vysledky hrace 1: {}".format(vysledky_1))
        b = random.randrange(1, 7)
        vysledky_2.append(b)
        hody.append(b)
        print("Vysledky hrace 2: {}".format(vysledky_2))
        c = random.randrange(1, 7)
        vysledky_3.append(c)
        hody.append(c)
        print("Vysledky hrace 3: {}".format(vysledky_3))
        d = random.randrange(1, 7)
        vysledky_4.append(d)
        hody.append(d)
        print("Vysledky hrace 4: {}".format(vysledky_4))
        mx = max(hody)
        if a == mx:
            vyherci.append("hrac 1")
            hrac1 = hrac1 + 1
        if b == mx:
            hrac2 = hrac2 + 1
        if c == mx:
            vyherci.append("hrac 3")
            hrac3 = hrac3 + 1
        if d == mx:
            vyherci.append("hrac 4")
            hrac4 = hrac4 + 1
        if len(vyherci) == 1:
            print("Vitez kola {} je: {}".format(kolo, vyherci))
        else:
            print("Vitezi kola {} jsou: {}".format(kolo, vyherci))
        kolo = kolo + 1
        vyherci.clear()
        hody.clear()
    skore.extend([hrac1, hrac2, hrac3, hrac4])
    mx = max(skore)
    if hrac1 == mx:
        vyherci.append("hrac 1")
    if hrac2 == mx:
        vyherci.append("hrac 2")
    if hrac3 == mx:
        vyherci.append("hrac 3")
    if hrac4 == mx:
        vyherci.append("hrac 4")
    if len(vyherci) == 1:
        print("Celkovy vitez je: {}".format(vyherci))
    else:
        print("Celkovymi vitezi jsou: {}".format(vyherci))


hraci(kolo)
