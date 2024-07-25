#Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
num = float(input('Insira o valor: '))
des = num - (num * 0.12)
print(f'O valor com desconto é {des}')