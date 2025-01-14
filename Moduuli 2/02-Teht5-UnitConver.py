import math

Leiviskät = float(input("Anna leivisköiden määrä = "))

Naulat = float(input("Anna naulojen määrä = "))

Luodit = float(input("Anna luotien määrä = "))

Muunnos1 = (Leiviskät * 20)

Muunnos2 = (Naulat + Muunnos1) * 32

Muunnos3 = float((Muunnos2 + Luodit) * 13.3)

Kilot = int(Muunnos3 / 1000)

Grammat = Muunnos3 % 1000

Grammat = round(Grammat, 2)

print("Massa modernien mittojen mukaan:",Kilot, "Kiloa", "ja", Grammat, "Grammaa")

