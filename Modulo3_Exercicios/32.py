#Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
numero = int(input('Insira um numero: '))
ante = numero - 1
suc = numero + 1
soma = (suc*3) + (ante*2)
print(f'O resultado é {soma}')