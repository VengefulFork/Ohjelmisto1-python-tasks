
while True :
    vuosi = input("Syötä vuosi = ")
    try:
        vuosi = int(vuosi)

    except:
        print("Ole hyvä ja syötä vuosi numeroina")

        continue

    if vuosi < 1 :
        print("Anna positiivinen vuosiluku")
        continue
    break

if vuosi % 400 == 0 :
    print("Vuosi", vuosi, "on karkausvuosi")
elif (vuosi % 4 == 0) and (vuosi % 100 != 0):
    print("Vuosi", vuosi, "on karkausvuosi")
else :
    print("Vuosi", vuosi, "ei ole karkausvuosi")