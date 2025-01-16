
while True :
    Vuosi = input("Syötä vuosi = ")
    try:
        Vuosi = int(Vuosi)

    except:
        print("Ole hyvä ja syötä vuosi numeroina")

        continue

    if Vuosi < 1 :
        print("Anna positiivinen vuosiluku")
        continue
    break

if (Vuosi % 400 == 0 ) and (Vuosi % 100 == 0):
    print("Vuosi",Vuosi,"on karkausvuosi")
elif (Vuosi % 4 == 0) and (Vuosi % 100 != 0):
    print("Vuosi",Vuosi,"on karkausvuosi")
else :
    print("Vuosi",Vuosi,"ei ole karkausvuosi")