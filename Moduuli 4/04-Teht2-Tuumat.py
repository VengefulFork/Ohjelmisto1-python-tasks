
while True :
    luku = input("Anna Tuumien määrä tai syötä negatiivinen luku pysäytääksesi \n= ")
    try:
        luku = float(luku)
    except :
        print("Syötä numero kiitos")
        continue

    if luku >= 1:
        Cm = luku * 2.54
        print("Tuumat senttimetreissä on",Cm,"cm")
        continue
    elif luku <= 0:
        print("Negatiivinen luku tunnistettu pysäytetään")
        break






