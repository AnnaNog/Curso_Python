import math

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

if a != 0:
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print ('Não existe raiz')
    elif delta == 0:
        x = -b / (2 * a)
        print (f'{x} é raiz única')
    else:
        x1 = ((-b) + math.sqrt(delta)) / (2 * a) 
        x2 = ((-b) - math.sqrt(delta)) / (2 * a) 
        print (f'A primeira raiz é {x1} e a segunda raiz é {x2}')
else:
    print('Não é uma equação de segundo grau')
