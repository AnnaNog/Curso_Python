#Faça um programa que receba dois números e mostre qual deles é o maior
num1 = float(input('Insira um numero: '))
num2 = float(input('Insira outro numero: '))

if num1 > num2:
    print(f'O numero {num1} é maior que o {num2}')
elif num1 < num2:
    print(f'O numero {num2} é maior que o {num1}')
else:
    print('Os números são iguais')