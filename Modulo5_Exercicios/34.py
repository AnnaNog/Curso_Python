#34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20? Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.

import math

mmc = 1

for i in range(1, 21):
    mmc = (mmc * i) // math.gcd(mmc, i)

print(mmc)