#Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
ano = int(input('Insira o ano atual: '))
idade = int(input('Insira a sua idade: '))
nasc = ano - idade
print(f'O ano que você nasceu é {nasc}')