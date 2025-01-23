import math
import random

lista = random.sample(range(1,100),random.randint(3,6))

lista.sort()

listan_summa = sum(lista)
listan_summa2 = 0

for i in lista :
    listan_summa2 += i


print(lista)
print(listan_summa)
print(listan_summa2)