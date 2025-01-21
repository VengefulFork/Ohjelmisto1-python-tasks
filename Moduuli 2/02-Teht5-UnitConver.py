import math

leiviskät = float(input("Anna leivisköiden määrä = "))

naulat = float(input("Anna naulojen määrä = "))

luodit = float(input("Anna luotien määrä = "))
#Muunnetaan Leiviskät Nauloiksi
muunnos1 = (leiviskät * 20)
#Lisätään muunnetut leiviskät annettuihin nauloihin ja muunnetaan ne luodeiksi
muunnos2 = (naulat + muunnos1) * 32
#Lisätään muunnetut luoteihin ja muutetaan  ne grammoiksi
muunnos3 = float((muunnos2 + luodit) * 13.3)
#Muunnokset Kiloiksi ja grammoiksi
kilot = int(muunnos3 / 1000)

grammat = muunnos3 % 1000

grammat = round(grammat, 2)

print("Massa modernien mittojen mukaan:", kilot, "Kiloa", "ja", grammat, "Grammaa")

