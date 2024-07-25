#Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.
n = int(input("Digite um número inteiro: "))

if n > 0:
    soma = 0
    for i in range(1, n + 1):
        soma = i + soma
    print(f"A soma dos {n} primeiros números naturais é: {soma}")
