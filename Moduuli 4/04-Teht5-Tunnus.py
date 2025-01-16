Tunnus = "python"

Salasana = "rules"

VäärätYritykset = 0


while VäärätYritykset < 5 :
    TunnusYritys = input("Kirjoita tunnus = ")

    SalasanaYritys = input("Kirjoita salasana = ")

    if TunnusYritys == Tunnus and SalasanaYritys == Salasana :
        print("Tervetuloa")
        break
    elif TunnusYritys != Tunnus or SalasanaYritys != Salasana:
        VäärätYritykset = VäärätYritykset + 1
        continue
if VäärätYritykset >=5 :
    print("Pääsy evätty")