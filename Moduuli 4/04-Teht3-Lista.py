

while True:
    NumeroLista = []
    Numero = input("Syötä numero tai tyhjä pysäytääksesi \n= ")
    try:
        if float(Numero):
            NumeroLista.append(Numero)
            continue
    except :
        if Numero == " " or "":
            print("Pysäytetään")
            NumeroLista.sort()
            print(NumeroLista)
            break
        else :
            continue










