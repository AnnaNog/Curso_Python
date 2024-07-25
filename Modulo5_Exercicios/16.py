#Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem decrescente.
n = int(input("Digite um número inteiro e ímpar: "))

if n > 0 and n % 2 != 0:
    while n > 0:
        print(n)
        n = n - 2