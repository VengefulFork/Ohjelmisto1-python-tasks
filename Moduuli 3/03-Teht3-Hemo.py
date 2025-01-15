Sukupuoli = input("Anna sukupuolesi = ")
Hemo = float(input("Anna Hemoglobiini arvosi = "))

Sukupuoli = Sukupuoli.lower()

if Sukupuoli == "nainen" and 117<=Hemo<=175:
    print("Normaali Hemoglobiini arvo naiselle")
elif Sukupuoli == "nainen" and Hemo<=116:
    print("test")
elif Sukupuoli == "nainen" and Hemo>=176:
    print("test2")
elif Sukupuoli == "mies" and 134<=Hemo<=195:
    print("test3")