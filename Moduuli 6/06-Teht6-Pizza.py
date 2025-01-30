from math import pi

halkaisija = float(input("= "))

hinta = float(input("= "))

def laskin(halkaisija, hinta):
    pinta_ala = pi * (halkaisija/2) ** 2

    hinta = hinta * 100

    hinta_per_neliometri = hinta / pinta_ala
    hinta_per_neliometri = round(hinta_per_neliometri, 2)
    return hinta_per_neliometri

print(laskin(halkaisija, hinta))