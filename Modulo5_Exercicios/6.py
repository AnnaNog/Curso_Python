#Faça um programa que leia 10 inteiros e imprima sua média
qtd = 10
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'Informe o {n}/{qtd} valor: ')) 
    soma = soma + numero
    media = soma / 10
print(f'A média é {media}')