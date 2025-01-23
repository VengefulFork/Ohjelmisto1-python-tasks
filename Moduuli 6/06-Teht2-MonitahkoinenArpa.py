import math
import random

tahkot = int(input("Anna nopan tahkojen määrä = "))


def arpa(tahkot):
    arvan_luku = random.randint(1,tahkot)
    return arvan_luku

flag = True

while flag :
    nopan_luku = arpa(tahkot)

    if nopan_luku == tahkot:
        flag = False


    print(nopan_luku)
