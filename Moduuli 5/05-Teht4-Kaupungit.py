kaupungit_lista = []

for i in range(5):
    kaupungit = input("Anna kaupungin nimi = ")
    kaupungit_lista.append(kaupungit)


for kaupungit_lista in kaupungit_lista:
    print(kaupungit_lista)

# Tämäkin toimii
for i in kaupungit_lista[:5]:
    print(i)