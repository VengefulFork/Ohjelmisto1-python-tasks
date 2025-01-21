sukupuoli = input("Anna sukupuolesi = ")
hemo = float(input("Anna Hemoglobiini arvosi = "))

sukupuoli = sukupuoli.lower()

if sukupuoli == "nainen" and 117<=hemo<=175:
    print("Normaali Hemoglobiini arvo naiselle")
elif sukupuoli == "nainen" and hemo<=116:
    print("Alhainen Hemoglobiini arvo naiselle")
elif sukupuoli == "nainen" and hemo>=176:
    print("Korkea Hemoglobiini arvo naiselle")
elif sukupuoli == "mies" and 134<=hemo<=195:
    print("Normaali Hemoglobiini arvo miehelle")
elif sukupuoli == "mies" and hemo<=134:
    print("Alhainen Hemoglobiini arvo miehelle")
elif sukupuoli == "mies" and hemo>=196:
    print("Korkea Hemoglobiini arvo miehelle")
else :
    print ("Ei hyväksyttyjä arvoja syötetty kokeile uudestaan")