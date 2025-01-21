import random
import math

def arpa():
    arvan_luku = random.randint(1,6)
    return arvan_luku


flag = True
while flag:
    luku = arpa()
    if luku == 6:
        flag = False
        print(luku)
    else:
        print(luku)
