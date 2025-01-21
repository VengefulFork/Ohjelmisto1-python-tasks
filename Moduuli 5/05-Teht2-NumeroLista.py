import math

loop = "o"

Lista = [0.0]

while loop != "":
    Numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
    try:
        if float(Numero):
            Lista.append(Numero)

            continue
    except:
        if Numero == "":
            loop = Numero

NumeroLista = [float(i) for i in Lista]

NumeroLista.sort(reverse=True)
Lista.sort()
#Metodi Yksi
# print(FloatList[:5])
#Metodi Kaksi
for i in NumeroLista[:5]:
    print(i)

print(Lista)
