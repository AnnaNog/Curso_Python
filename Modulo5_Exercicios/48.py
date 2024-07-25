#Faça um programa que some o termo de valor par da sequência de Fibonacci, cujos os valores não ultrapassem quatro milhões.

num = 4000000
soma = 0
anterior = 0
atual = 1

while atual <= num:
    if atual % 2 == 0:
        soma = soma + atual
    prox = anterior + atual
    anterior = atual
    atual = prox

print(f'A soma dos termos pares é {soma}')