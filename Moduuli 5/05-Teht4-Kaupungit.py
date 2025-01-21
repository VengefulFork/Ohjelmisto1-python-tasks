KaupungitLista = []

for i in range(5):
    Kaupungit = input("Anna kaupungin nimi = ")
    KaupungitLista.append(Kaupungit)


for KaupungitLista in KaupungitLista:
    print(KaupungitLista)

# Tämäkin toimii
# for i in KaupungitLista[:5]:
#     print(i)