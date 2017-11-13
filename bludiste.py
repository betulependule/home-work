#! /usr/bin/env python3

import random

blud = []
pocet = 26
kolo = pocet / 2


def sablona(blud, pocet):
    for x in range(pocet):
        blud.append([])
        for x in range(pocet):
            blud[-1].append(0)


def labyrint(blud, pocet, kolo):
    for x in blud[-1]:
        while 2 not in blud[-1]:
            if kolo == pocet:
                kolo = 1
            if kolo != 0 and kolo != pocet:
                blud[-1][int(kolo)] = random.choice([0, 2])
            kolo = kolo + 1
        s = blud[-1].index(2)
        blud[-2][s] = 1
    for x in blud:
        while 3 not in x:
            for x in list(reversed(blud)):
                for y in x:
                    a = blud.index(x)
                    b = x.index(y)
                    c = random.randrange(10)
                    if (
                        y == 1 and
                        c >= 6 and
                        blud.index(x) > 2 and
                        blud[a - 1][b] == 0
                    ):
                        blud[a - 1][b] = 1
                        blud[a - 2][b] = 1
                        blud[a][b] = 2
                    elif (
                        y == 1 and
                        7 >= c >= 5 and
                        blud.index(x) < pocet - 4 and
                        blud[a + 1][b] == 0
                    ):
                        blud[a + 1][b] = 1
                        blud[a + 2][b] = 1
                        blud[a + 3][b] = 1
                        blud[a][b] = 2
                    elif (
                        y == 1 and
                        3 >= c >= 3 and
                        x.index(y) > 3 and
                        blud[a][b - 1] == 0
                    ):
                        blud[a][b - 1] = 1
                        blud[a][b - 2] = 1
                        blud[a][b - 3] = 1
                        blud[a][b] = 2
                    elif (
                        y == 1 and
                        x.index(y) < pocet - 4 and
                        blud[a][b + 1] == 0
                    ):
                        blud[a][b + 1] = 1
                        blud[a][b + 2] = 1
                        blud[a][b] = 2
                    if (
                        blud.index(x) < pocet - 2 and
                        blud[a - 1][b] != 0 and
                        blud[a + 1][b] != 0 and
                        blud[a][b - 1] != 0 and
                        blud[a][b + 1] != 0
                    ):
                        blud[a][b] = 0
                    if (
                        (y == 1 or y == 2) and
                        blud.index(x) == 1
                    ):
                        blud[a - 1][b] = 3
                        return blud


def uprava(blud):
    for x in blud:
        while 2 in x:
            for x in blud:
                for y in x:
                    a = blud.index(x)
                    b = x.index(y)
                    if y == 3:
                        blud[a][b] = 1
                    if y == 2:
                        blud[a][b] = 1
    print(blud)


def zobrazeni(blud, pocet):
    kolo = 1
    for x in blud:
        for y in x:
            if kolo == pocet:
                print(""),
                kolo = 1
            elif y == 0:
                print("X", end="")
                kolo = kolo + 1
            else:
                print(" ", end="")
                kolo = kolo + 1


sablona(blud, pocet)
labyrint(blud, pocet, kolo)
uprava(blud)
zobrazeni(blud, pocet)
