import math
import random

summa = []

noppa_määrä = int(input("Anna noppien määrä numeroin = "))

for i in range(noppa_määrä):
    summa.append(int(random.randint(1,6)))
    listan_summa = sum(summa)

print(summa)
print(listan_summa)


