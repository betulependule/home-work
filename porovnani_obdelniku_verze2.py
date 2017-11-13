#! /usr/bin/env python3

a_1 = 2
b_1 = 2
o_1 = 2 * a_1 + 2 * b_1
S_1 = a_1 * b_1
a_2 = 4
b_2 = 1
o_2 = 2 * a_2 + 2 * b_2
S_2 = a_2 * b_2

if S_1 == S_2:
    if o_1 == o_2:
        print("obdelniky jsou totozne")
    elif o_1 > o_2:
        print("obdelniky maji shodnou plochu, ale obdelnik 1 ma vetsi obvod")
    elif o_1 < o_2:
        print("obdelniky maji shodnou plochu, ale obdelnik 2 ma vetsi obvod")
elif o_1 == o_2:
    if S_1 > S_2:
        print("obdelniky maji shodny obvod, ale obdelnik 1 ma vetsi plochu")
    elif S_1 < S_2:
        print("obdelniky maji shodny obvod, ale obdelnik 2 ma vetsi plochu")
else:
    print("obdelniky nemaji stejny obvod ani obsah")
