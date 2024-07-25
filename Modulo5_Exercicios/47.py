# Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:

#adição (opção 1)
#subtração (opção 2)
#multiplicação (opção 3)
#divisão (opção 4)
#saída (opção 5)

#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).

opcao = 0

while opcao != 5:
    print('Opção 1 - adição')
    print('Opção 2 - subtração')
    print('Opção 3 - multiplicação')
    print('Opção 4 - divisão')
    print('Opção 5 - sair')
    opcao = int(input('Digite a opção desejada:'))
    if opcao == 1:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        soma = num1 + num2
        print(f'A soma é {soma}')
    elif opcao == 2:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        sub = num1 - num2
        print(f'A subtração é {sub}')
    elif opcao == 3:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        mul = num1 * num2
        print(f'A multiplicação é {mul}')
    elif opcao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        div = num1 / num2
        print(f'A divisão é {div}')
