import math
Lippu = True
Luku = int(input("Anna luku = "))

if Luku > 1:

        for i in range(2, Luku):
                if (Luku % i ) == 0:
                        Lippu = False


if Lippu:
        print("On alkuluku")
else :
        print("Ei ole alkuluku")
