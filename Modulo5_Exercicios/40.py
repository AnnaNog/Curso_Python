# Elabore um programa que faça leitura de vários números inteiros até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

num = int(input('Digite o número: '))

if num >= 0:
    menor = num
    maior = num

else: 
    print('Insira somente números positivos')

while num >= 0:
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
    num = int(input('Digite o número: '))

print(f'O maior número é {maior} e o menor é {menor}')