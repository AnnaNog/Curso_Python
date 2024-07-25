# Faça um programa que leia vários números, calcule e mostre: (a) A soma dos números digitados (b) A quantidade de números digitados (c) O maior número digitado (d) O menor número digitado (e) A média dos números pares Finalize a entrada de dados caso o usuário informe o valor 0.

soma = 0
quantidade = 0
soma_pares = 0
quantidade_pares = 0

num = int(input('Digite um número: '))

if num == 0:
    print('Digite um número válido')
else:
    maior = num
    menor = num

    while num != 0:
        soma = soma + num
        quantidade = quantidade + 1

        if num > maior:
            maior = num

        if num < menor:
            menor = num

        if num % 2 == 0:
            soma_pares = soma_pares + num
            quantidade_pares = quantidade_pares + 1

        num = int(input('Digite um número: '))

    print(f'Soma dos números é {soma}, a quantidade de números digitados é {quantidade}, o maior número digitado é {maior} e o menor é {menor}')

    if quantidade_pares > 0:
        media_pares = soma_pares / quantidade_pares
        print(f'A média dos pares é {media_pares}')