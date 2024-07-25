#Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a relação entre eles (>, <, =) de cada lançamento.

import random

igual = 0
maior = 0
menor = 0

n = 15

for _ in range(n):
        # Lança dois dados
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    if d1 == d2:
            igual = igual + 1
            relation = "="
    elif d1 > d2:
        maior = maior + 1
        relation = ">"
    else:
        menor = menor + 1
        relation = "<"

    print(f"d1: {d1}, d2: {d2}, Relação: {relation}")

print(f"Igual: {igual} vezes")
print(f"Maior: {maior} vezes")
print(f"Menor: {menor} vezes")
