#! /usr/bin/env python3

import random
kolo = 1


def hraci(kolo):
    vysledky_1 = []
    vysledky_2 = []
    vysledky_3 = []
    vysledky_4 = []
    hrac1 = 0
    hrac2 = 0
    hrac3 = 0
    hrac4 = 0
    while kolo <= 5:
        a = random.randrange(1, 7)
        vysledky_1.append(a)
        print("Vysledky hrace 1: {}".format(vysledky_1))
        b = random.randrange(1, 7)
        vysledky_2.append(b)
        print("Vysledky hrace 2: {}".format(vysledky_2))
        c = random.randrange(1, 7)
        vysledky_3.append(c)
        print("Vysledky hrace 3: {}".format(vysledky_3))
        d = random.randrange(1, 7)
        vysledky_4.append(d)
        print("Vysledky hrace 4: {}".format(vysledky_4))
        if a > b and a > c and a > d:
            print("Hrac 1 je vitezem kola {} se skorem {}.".format(kolo, a))
            hrac1 = hrac1 + 1
        elif b > a and b > c and b > d:
            print("Hrac 2 je vitezem kola {} se skorem {}.".format(kolo, b))
            hrac2 = hrac2 + 1
        elif c > a and c > b and c > d:
            print("Hrac 3 je vitezem kola {} se skorem {}.".format(kolo, c))
            hrac3 = hrac3 + 1
        elif d > a and d > c and d > b:
            print("Hrac 4 je vitezem kola {} se skorem {}.".format(kolo, d))
            hrac4 = hrac4 + 1
        elif a == b and a > c and a > d:
            print("Hraci 1 a 2 jsou vitezi kola {} se skorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac2 = hrac2 + 1
        elif a == c and a > b and a > d:
            print("Hraci 1 a 3 jsou vitezi kola {} se skorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac3 = hrac3 + 1
        elif a == d and a > c and a > b:
            print("Hraci 1 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac4 = hrac4 + 1
        elif b == c and b > a and b > d:
            print("Hraci 2 a 3 jsou vitezi kola {} se skorem {}."
                  .format(kolo, b))
            hrac3 = hrac3 + 1
            hrac2 = hrac2 + 1
        elif b == d and b > c and b > a:
            print("Hraci 2 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, b))
            hrac4 = hrac4 + 1
            hrac2 = hrac2 + 1
        elif c == d and c > b and c > a:
            print("Hraci 3 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, c))
            hrac3 = hrac3 + 1
            hrac2 = hrac2 + 1
        elif a == b == c and a > d:
            print("Hraci 1, 2 a 3 jsou vitezi kola {} seskorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac2 = hrac2 + 1
            hrac3 = hrac3 + 1
        elif a == b == d and a > c:
            print("Hraci 1, 2 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac2 = hrac2 + 1
            hrac4 = hrac4 + 1
        elif b == c == d and b > a:
            print("Hraci 2, 3 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, b))
            hrac4 = hrac4 + 1
            hrac2 = hrac2 + 1
            hrac3 = hrac3 + 1
        elif a == c == d and a > b:
            print("Hraci 1, 3 a 4 jsou vitezi kola {} se skorem {}."
                  .format(kolo, a))
            hrac1 = hrac1 + 1
            hrac4 = hrac4 + 1
            hrac3 = hrac3 + 1
        kolo = kolo + 1
    if hrac1 > hrac2 and hrac1 > hrac3 and hrac1 > hrac4:
        print("Hrac 1 je celkovym vitezem.")
    elif hrac2 > hrac1 and hrac2 > hrac3 and hrac2 > hrac4:
        print("Hrac 2 je celkovym vitezem.")
    elif hrac3 > hrac1 and hrac3 > hrac2 and hrac3 > hrac4:
        print("Hrac 3 je celkovym vitezem.")
    elif hrac4 > hrac1 and hrac4 > hrac3 and hrac4 > hrac2:
        print("Hrac 4 je celkovym vitezem.")
    elif hrac1 == hrac2 and hrac1 > hrac3 and hrac1 > hrac4:
        print("Hraci 1 a 2 jsou celkovymi vitezi.")
    elif hrac1 == hrac3 and hrac1 > hrac2 and hrac1 > hrac4:
        print("Hraci 1 a 3 jsou celkovymi vitezi.")
    elif hrac1 == hrac4 and hrac1 > hrac3 and hrac1 > hrac2:
        print("Hraci 1 a 4 jsou celkovymi vitezi.")
    elif hrac2 == hrac3 and hrac2 > hrac1 and hrac2 > hrac4:
        print("Hraci 2 a 3 jsou celkovymi vitezi.")
    elif hrac2 == hrac4 and hrac2 > hrac3 and hrac2 > hrac1:
        print("Hraci 2 a 4 jsou celkovymi vitezi.")
    elif hrac3 == hrac4 and hrac3 > hrac2 and hrac3 > hrac1:
        print("Hraci 3 a 4 jsou celkovymi vitezi.")
    elif hrac1 == hrac2 == hrac3 and hrac1 > hrac4:
        print("Hraci 1, 2 a 3 jsou celkovymi vitezi.")
    elif hrac1 == hrac2 == hrac4 and hrac1 > hrac3:
        print("Hraci 1, 2 a 4 jsou celkovymi vitezi.")
    elif hrac2 == hrac3 == hrac4 and hrac2 > hrac1:
        print("Hraci 2, 3 a 4 jsou celkovymi vitezi.")
    elif hrac1 == hrac3 == hrac4 and hrac1 > hrac2:
        print("Hraci 1, 3 a 4 jsou celkovymi vitezi.")


hraci(kolo)
