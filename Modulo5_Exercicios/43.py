#Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), e calcule a idade média desse grupo.

idade = int(input('Digite uma idade: '))
contador = 0
soma = 0

while idade != 0:
    soma = soma + idade
    contador = contador + 1
    idade = int(input('Digite uma idade: '))

if contador > 0:
    media = soma / contador
    print(f'A média é {media} anos')

else: 
    print('Nenhuma idade válida informada')
