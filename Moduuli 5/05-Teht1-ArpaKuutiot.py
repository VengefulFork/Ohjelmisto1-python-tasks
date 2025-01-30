import math
import random

noppien_silmäluvut = []

noppa_määrä = int(input("Anna noppien määrä numeroin = "))

for i in range(noppa_määrä):
    noppien_silmäluvut.append(int(random.randint(1, 6)))
    listan_summa = sum(noppien_silmäluvut)
# Tulostetaan kaikkien heitettyjen noppien silmäluvut, lähinnä testausta varten
print("Heitettyjen noppien silmäluvut ovat",noppien_silmäluvut)
# Tulostestaan noppien silmälukujen summa
print("Kaikkien heitettyjen noppien silmälukujen summa on",listan_summa)


