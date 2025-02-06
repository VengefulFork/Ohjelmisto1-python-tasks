
lentokentät = {}

käsky = ""

while käsky != "lopeta":

    käsky = str(input("Kirjoita lisää jos haluat lisätä, hae jos haluat hakea tai lopeta jos haluat lopettaa = "))

    käsky = käsky.lower()

    if käsky == "lisää" :
        icao = str(input("\nAnna lentokentän ICAO koodi = ")).upper()

        kentän_nimi = str(input("\nAnna lentokentän nimi = ")).capitalize()

        lentokentät[icao] = kentän_nimi

    if käsky == "hae" :
        icao = str(input("Anna lentokentän ICAO koodi hakeaksesi = ")).upper()

        if icao in lentokentät:

            print("\nKentän nimi on", lentokentät[icao])
