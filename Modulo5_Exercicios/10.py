#Escreva um programa que calcule e mostre a soma dos 50 primeiros números pares

soma = 0
conta = 0
num = 2

n = 50

while conta < n:
    soma = soma + num
    conta = conta + 1
    num = num + 2


print(f"A soma dos primeiros {n} números pares é {soma}.")
