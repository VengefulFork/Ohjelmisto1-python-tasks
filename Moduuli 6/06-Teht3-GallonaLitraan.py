import math


litrat = float()


def muunnin(gallonat):
    muunnos = gallonat * 3.785
    return muunnos

while True :
    gallonat = float(input("Anna gallonat tai negatiivinen luku pysäytääksesi = "))
    if gallonat <= 0 :
        print("Pysäytetään")
        break
    else :
        litrat = muunnin(gallonat)
        print(f"{gallonat} gallonaa on {litrat:6.3f} litraa")
