import random

numero = random.randint(1, 10)


while True:
    arvaus = (input("Arvaa numero = "))
    try:
        arvaus = int(arvaus)
    except :
        print("Syötä numero kiitos")
        continue

    if arvaus > numero:
        print("Arvaus on Suurempi kuin vastaus")
        continue
    elif arvaus < numero:
        print("Arvaus on pienempi kuin vastaus")
        continue
    elif arvaus == numero:
        print("Arvasit oikein! Vastaus oli", numero)
        break

