#Escreva uma algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números lidos deve ser fornecida pelo usuário

quant = int(input('Digite a quantidade de números que devem ser lidos: '))

maior_num = int(input('Digite o número: '))
contagem_maior = 1

for i in range(1, quant):
    num = int(input('Digite o número: '))
    if num > maior_num:
        maior_num = num
        contagem_maior = 1
    elif num == maior_num:
        contagem_maior = contagem_maior + 1

print(f'O maior número é {maior_num} e foi repetido {contagem_maior} vezes')
