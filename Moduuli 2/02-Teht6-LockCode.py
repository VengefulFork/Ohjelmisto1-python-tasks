import random




LukkoKoodi1 = (random.sample(range(1,10), 3))
LukkoKoodi2 = (random.sample(range(1,7), 4))

print("\nLukon Yksi koodi on =",LukkoKoodi1,"Lukon kaksi koodi on = ", LukkoKoodi2)


#Toinen tapa tehdä käyttäen for ja random.randint
LukkoKoodi3 = []
LukkoKoodi4 = []
for i in range(3):
    numero = random.randint(1,9)
    LukkoKoodi3.append(numero)

for a in range(4):
    numero2 = random.randint(1,6)
    LukkoKoodi4.append(numero2)

print("\nToisella tavalla luodut koodit ovat =", LukkoKoodi3,"ja",LukkoKoodi4)


#Kolmas tapa
LukkoKoodi5 = []
LukkoKoodi6 = []

Toistot = 0

while Toistot < 7:

    if Toistot < 3:
        numero3 = random.randint(1,9)
        LukkoKoodi5.append(numero3)
        Toistot = Toistot +1
        continue
    elif Toistot < 7:
        numero4 = random.randint(1,6)
        LukkoKoodi6.append(numero4)
        Toistot = Toistot +1

print("\nKolmanella Tavalla luodut ovat =",LukkoKoodi5,"ja",LukkoKoodi6)