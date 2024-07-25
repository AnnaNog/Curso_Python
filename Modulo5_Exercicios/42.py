#Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math

num = float(input('Digite um número: '))

while num > 0:
    quadrado = num ** 2
    cubo = num ** 3
    raiz = math.sqrt(num)
    print(f'O quadrado é {quadrado}, o cubo é {cubo} e a raiz é {raiz}')
    num = float(input('Digite um número: '))