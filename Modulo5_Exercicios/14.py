#Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.
n = int(input("Digite um número inteiro e par: "))

if n >= 0 and n % 2 == 0:
    while n >= 0:
        print(n)
        n = n - 2
