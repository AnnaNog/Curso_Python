#Escreva um programa para calcular o valor da série, para 5 termos:
# S=0+ 1/2! + 2/4! + 3 /6! + ....

import math

n = 5
soma = 0

for i in range (n):
    s = i / ((math.factorial(2*i)))
    soma = soma + s
print (soma)