import math

loop = True

lista = []
    
while loop :
    numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
    try:
        if float(numero):
            lista.append(float(numero))

            continue
    except:
        if numero == "":
            loop = False


lista.sort(reverse=True)
# Lista.sort()
#Testausta varten
print(lista[:5])
#Varsinainen printtaus
for i in lista[:5]:
    print(i)

# print(Lista)
