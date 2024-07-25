#Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente
n = int(input("Digite um número inteiro: "))

if n >= 0:
    conta = 0
    while conta <= n:
        print(conta)
        conta = conta + 1