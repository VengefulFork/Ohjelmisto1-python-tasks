import math
import random



# Funktio listan numeroiden summan laskemiseen
def summa_funktio(numero_lista):
    listan_summa = 0

    for i in numero_lista:
        listan_summa += i
    return listan_summa

# Numero listan luominen
numero_lista = random.sample(range(1,101),random.randint(3,6))

# Printataan koko lista, jotta voidaan tarkistaa onko annettu summa oikea
print("Lista numeroita",numero_lista)
# Kutsutaan funktio ja printataan sen antama tulos
print("\nListan numeroiden summa",summa_funktio(numero_lista))
