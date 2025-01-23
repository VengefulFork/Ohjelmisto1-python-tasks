import math

loop = True

suurin_luku = float()
pienin_luku = float()

toisto_yksi = True

while loop :
    annettu_luku = input("Anna jokin luku tai tyhjä pysäyttääksesi= ")

    try :
        annettu_luku = float(annettu_luku)
        if toisto_yksi :
            suurin_luku = pienin_luku = annettu_luku
            toisto_yksi = False
        else :
            if annettu_luku < pienin_luku :
                pienin_luku = annettu_luku
            elif annettu_luku > suurin_luku:
                suurin_luku = annettu_luku

    except:
        if annettu_luku == "":
            loop = False
        else :
            print("Ei hyväksytty input")


print ("Suurin luku on",suurin_luku, "Pienin luku on",  pienin_luku)


# Listaa käyttäen toisenlainen ratkaisu

# loop = "o"
#
# numero_lista = []
#
# while loop != "":
#     numero = input("Anna numero jatkaaksesi tai tyhjä lopetaaksesi = ")
#     try:
#         if float(numero):
#             numero_lista.append(float(numero))
#
#             continue
#     except:
#         if numero == "":
#             loop = numero
#
# numero_lista.sort()
# print("Pienin luku on", numero_lista[0], "Suurin luku on", numero_lista[-1])







