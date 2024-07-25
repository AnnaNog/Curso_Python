#Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir:
# E=1+1/1!+1/2!+1/3!+...+1/N!

import math

n = int(input('Insira um número: '))

if n >= 0:
    e = 1
    for i in range (1, n + 1):
        e = e + 1 / math.factorial(i)
print (e)