#Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.
n = int(input("Digite um número inteiro e par: "))

if n >= 0 and n % 2 == 0:
    num = 2
    while num <= n:
        print(num)
        num = num + 2
        
