sexo = (input('Insira seu sexo (f/m): '))
altura = float(input('Insira sua altura: '))


if sexo.lower() == 'f':
    f = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {f}')

else: 
    m = (72.7 * altura) - 58
    print(f'Seu peso ideial é {m}')