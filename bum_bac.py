#! /usr/bin/env python3


def bum_bac():
    cislo1 = int(input("Napiste prvni libovolne cislo: "))
    cislo2 = int(input("Napiste druhe libovolne cislo: "))
    posloupnost = range(cislo1, cislo2, 1)
    a = "bum"
    b = "bac"
    for x in posloupnost:
        if x % 2 == 0 and x % 6 == 0:
            print(a + b)
        elif x % 6 == 0:
            print(b)
        elif x % 2 == 0:
            print(a)
        else:
            print(x)


bum_bac()
