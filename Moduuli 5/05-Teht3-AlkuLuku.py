import math
lippu = True
luku = int(input("Anna luku = "))

if luku > 1:

        for i in range(2, luku):
                if (luku % i) == 0:
                        lippu = False


if lippu:
        print("On alkuluku")
else :
        print("Ei ole alkuluku")
