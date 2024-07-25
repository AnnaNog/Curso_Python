#Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido


menor = float(input("Digite o 1º número: "))
maior = menor

for _ in range(9):
    num = float(input(f"Digite o {_+2}º número: "))
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

    print(f"O menor valor lido foi: {menor}")
    print(f"O maior valor lido foi: {maior}")


