koko = float(input("Anna Kuhan pituus = "))
if koko>=37:
    print("Onnittelut Kuhasi on hyväksytyn mittainen")
if not koko >= 37:
    Alimitta = 37 - koko
    print("Kalastaja laske Kuhasi takaisin vesistöön, koska se on",Alimitta,"cm alle hyväksytyn mitan" )
