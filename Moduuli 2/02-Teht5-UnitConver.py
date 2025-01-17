

Leiviskät = float(input("Anna leivisköiden määrä = "))

Naulat = float(input("Anna naulojen määrä = "))

Luodit = float(input("Anna luotien määrä = "))
#Muunnetaan Leiviskät Nauloiksi
Muunnos1 = (Leiviskät * 20)
#Lisätään muunnetut leiviskät annettuihin nauloihin ja muunnetaan ne luodeiksi
Muunnos2 = (Naulat + Muunnos1) * 32
#Lisätään muunnetut luoteihin ja muutetaan  ne grammoiksi
Muunnos3 = float((Muunnos2 + Luodit) * 13.3)
#Muunnokset Kiloiksi ja grammoiksi
Kilot = int(Muunnos3 / 1000)

Grammat = Muunnos3 % 1000

Grammat = round(Grammat, 2)

print("Massa modernien mittojen mukaan:",Kilot, "Kiloa", "ja", Grammat, "Grammaa")

