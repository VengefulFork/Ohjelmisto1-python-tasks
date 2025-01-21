import math

loop = "o"

numero_lista = []

while loop != "":
    numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
    try:
        if float(numero):
            numero_lista.append(numero)

            continue
    except:
        if numero == "":
            loop = numero

float_list = [float(i) for i in numero_lista]

float_list.sort()

print("Pienin luku on", float_list[0], "Suurin luku on", float_list[-1])









