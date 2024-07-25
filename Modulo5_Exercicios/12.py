#Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente
n = int(input("Digite um número inteiro: "))

if n >= 0:
    while n >= 0:
        print(n)
        n = n - 1