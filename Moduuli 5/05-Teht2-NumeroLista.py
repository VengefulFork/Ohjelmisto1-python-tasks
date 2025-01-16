import math

loop = "o"

NumeroLista = []

while loop != "":
    Numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
    try:
        if float(Numero):
            NumeroLista.append(Numero)

            continue
    except:
        if Numero == "":
            loop = Numero

FloatList = [float(i) for i in NumeroLista]

FloatList.sort(reverse=True)

#Metodi Yksi
# print(FloatList[:5])
#Metodi Kaksi
for i in FloatList[:5]:
    print(i)

