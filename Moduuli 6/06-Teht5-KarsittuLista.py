import math
import random

# Funktio toisen listan luomiseen joka ei sisällä parittomia lukuja
def karsija(alkuperäinen_lista):
    karsittu_lista = []
    # Testataanko onko luku tasan jaollinen kahdella ja jos on lisätään uuteen listaan.
    for i in alkuperäinen_lista:
        if i % 2 == 0:
            karsittu_lista.append(int(i))


    return karsittu_lista

# Luodaan lista kokonaislukuja
alkuperäinen_lista = random.sample(range(1, 101), random.randint(3, 7))

print("Alkuperäinen kaikki luvut sisältävä lista",alkuperäinen_lista)
print("Ei parittomia lukuja sisältävä list",karsija(alkuperäinen_lista))