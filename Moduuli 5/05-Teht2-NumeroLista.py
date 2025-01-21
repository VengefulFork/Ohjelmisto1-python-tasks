import math

loop = True

lista = []

while loop :
    numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
    try:
        if float(numero):
            lista.append(numero)

            continue
    except:
        if numero == "":
            loop = False

numero_lista = [float(i) for i in lista]

numero_lista.sort(reverse=True)
# Lista.sort()
#Metodi Yksi
print(numero_lista[:5])
#Metodi Kaksi
for i in numero_lista[:5]:
    print(i)

# print(Lista)
