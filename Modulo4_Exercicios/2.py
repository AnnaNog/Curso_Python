import math

num = float(input('Insira um numero: '))

if num >= 0:
    raiz = math.sqrt(num)
    print(f'A raiz é {raiz}')
else:
    print('Numero invalido')