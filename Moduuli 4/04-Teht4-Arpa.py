import random

Numero = random.randint(1,10)
# Numero = 5

while True:
    Arvaus = (input("Arvaa numero = "))
    try:
        Arvaus = int(Arvaus)
    except :
        print("Syötä numero kiitos")
        continue

    if Arvaus > Numero:
        print("Arvaus on Suurempi kuin vastaus")
        continue
    elif Arvaus < Numero:
        print("Arvaus on pienempi kuin vastaus")
        continue
    elif Arvaus == Numero:
        print("Arvasit oikein! Vastaus oli",Numero)
        break

