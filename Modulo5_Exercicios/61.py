#Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de três dígitos. Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91 x 99.
maior = 0
num1 = 0
num2 = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        vezes = i * j
        if str(vezes) == str(vezes)[::-1]:
            if vezes > maior:
                maior = vezes
                num1 = i
                num2 = j

print(f'O maior é {maior}')