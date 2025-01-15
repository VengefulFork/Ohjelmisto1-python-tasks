Sukupuoli = input("Anna sukupuolesi = ")
Hemo = float(input("Anna Hemoglobiini arvosi = "))

Sukupuoli = Sukupuoli.lower()

if Sukupuoli == "nainen" and 117<=Hemo<=175:
    print("Normaali Hemoglobiini arvo naiselle")
elif Sukupuoli == "nainen" and Hemo<=116:
    print("Alhainen Hemoglobiini arvo naiselle")
elif Sukupuoli == "nainen" and Hemo>=176:
    print("Korkea Hemoglobiini arvo naiselle")
elif Sukupuoli == "mies" and 134<=Hemo<=195:
    print("Normaali Hemoglobiini arvo miehelle")
elif Sukupuoli == "mies" and Hemo<=134:
    print("Alhainen Hemoglobiini arvo miehelle")
elif Sukupuoli == "mies" and Hemo>=196:
    print("Korkea Hemoglobiini arvo miehelle")
else :
    print ("Ei hyväksyttyjä arvoja syötetty kokeile uudestaan")