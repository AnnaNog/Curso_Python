import math

num = float(input('Insira um numero: '))

if num >= 0:
    raiz = math.sqrt(num)
    quadrado = num ** 2
    print(f'A raiz é {raiz} e o quadrado é {quadrado}')
else:
    print(f'Numero inválido')