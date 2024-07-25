import math

num = int(input('Insira um numero: '))

if num < 0:
    print(f'Numero invalido')
else:
    log = math.log10(num)
    print(f'O log é {log}')