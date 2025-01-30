
lentokentät = {}

käsky = ""

while käsky != "lopeta":

    käsky = str(input("Kirjoita lisää jos haluat lisätä, hae jos haluat hakea tai lopeta jos haluat lopettaa = "))

    käsky = käsky.lower()

    if käsky == "lisää" :
        icao = str(input("\nAnna lentokentän ICAO koodi = "))

        icao.upper()

        kentän_nimi = str(input("\nAnna lentokentän nimi = "))

        kentän_nimi.capitalize()

        lentokentät[icao] = kentän_nimi

    if käsky == "hae" :
        icao = str(input("Anna lentokentän ICAO koodi hakeaksesi = "))

        if icao in lentokentät:

            print("\nKentän nimi on", lentokentät[icao])
