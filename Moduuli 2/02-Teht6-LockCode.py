import random




lukko_koodi1 = (random.sample(range(1, 10), 3))
lukko_koodi2 = (random.sample(range(1, 7), 4))

print("\nLukon Yksi koodi on =", lukko_koodi1, "Lukon kaksi koodi on = ", lukko_koodi2)


#Toinen tapa tehdä käyttäen for ja random.randint
lukko_koodi3 = []
lukko_koodi4 = []
for i in range(3):
    numero = random.randint(1,9)
    lukko_koodi3.append(numero)

for a in range(4):
    numero2 = random.randint(1,6)
    lukko_koodi4.append(numero2)

print("\nToisella tavalla luodut koodit ovat =", lukko_koodi3, "ja", lukko_koodi4)


#Kolmas tapa
lukko_koodi5 = []
lukko_koodi6 = []

toistot = 0

while toistot < 7:

    if toistot < 3:
        numero3 = random.randint(1,9)
        lukko_koodi5.append(numero3)
        toistot = toistot + 1
        continue
    elif toistot < 7:
        numero4 = random.randint(1,6)
        lukko_koodi6.append(numero4)
        toistot = toistot + 1

print("\nKolmanella Tavalla luodut ovat =", lukko_koodi5, "ja", lukko_koodi6)