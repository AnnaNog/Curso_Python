#Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
soma = 0
n = 1000

for i in range (1, n):
    if i % 3 == 0 or i % 5 == 0:
        soma = i + soma
print(soma)