Koko = float(input("Anna Kuhan pituus = "))
if Koko>=37:
    print("Onnittelut Kuhasi on hyväksytyn mittainen")
if not Koko>=37:
    Alimitta = 37 - Koko
    print("Kalastaja laske Kuhasi takaisin vesistöön, koska se on",Alimitta,"cm alle hyväksytyn mitan" )
