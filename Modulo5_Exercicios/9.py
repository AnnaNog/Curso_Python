#Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares
impares = 0
num = 1

N = int(input("Digite um número inteiro N: "))  

while impares < N:
    print(num)
    impares = impares + 1
    num = num + 2


