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

FloatList.sort()

print("Pienin luku on",FloatList[0],"Suurin luku on",FloatList[-1])









