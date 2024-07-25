#Faça um programa que peça ao usuário para digitar 10 valores e some-os
qtd = 10
soma = 0

for n in range(1, qtd+1):
    numero = float(input(f'Informe o {n}/{qtd} valor: ')) 
    soma = soma + numero
print(f'A soma é {soma}')