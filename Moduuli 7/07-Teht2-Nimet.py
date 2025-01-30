nimet = set()
nimi = "0"

while nimi != "":

    nimi = str(input("\nAnna jokin nimi tai paina enter pysäytääksesi = "))
    if nimi not in nimet and not nimi == "" :
        nimet.add(nimi)
        print("\nUusi nimi")
    elif nimi in nimet and not nimi == "" :
        print("\nAiemmin syötetty nimi")


for i in nimet:
    print(i)