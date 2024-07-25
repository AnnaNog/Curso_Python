#30. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

base = - 1
altura = -1 

while base <= 0:
    base = float(input('Insira um valor para a base: '))

while altura <= 0:
    altura = float(input('Insira um valor para a altura: '))

area = (base * altura) / 2
print(f"A área do triângulo é {area}")