import math

num = float(input('Insira um numero: '))

if num >= 0:
    raiz = math.sqrt(num)
    print(f'A raiz é {raiz}')
else:
    quadrado = num ** 2
    print(f'O numero ao quadrado é {quadrado}')