tunnus = "python"

salasana = "rules"

väärät_yritykset = 0


while väärät_yritykset < 5 :
    tunnus_yritys = input("Kirjoita tunnus = ")

    salasana_yritys = input("Kirjoita salasana = ")

    if tunnus_yritys == tunnus and salasana_yritys == salasana :
        print("Tervetuloa")
        break
    elif tunnus_yritys != tunnus or salasana_yritys != salasana:
        väärät_yritykset = väärät_yritykset + 1
        continue
if väärät_yritykset >=5 :
    print("Pääsy evätty")