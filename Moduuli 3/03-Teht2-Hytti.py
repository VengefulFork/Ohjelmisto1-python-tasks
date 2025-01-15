Hytti = input("Anna Hyttin luokka = ")
Hytti = Hytti.lower()
if Hytti == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif Hytti == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif Hytti == "b":
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif Hytti == "c":
    print ("C on ikkunaton hytti autokannen alapuolella.")
else :
    print("Ei hyvaksytty hyttiluokka")