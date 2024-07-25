media = (input('Escolha o tipo de média desejada:\n a - Geométrica\n b - Ponderada\n c - Harmônica\n d - Aritmética\n '))
x = int(input('Insira o x: '))
y = int(input('Insira o y: '))
z = int(input('Insira o z: '))


if x > 0 and y > 0 and z > 0:
    if media.lower() == 'a':
        geo = (x * y * z) ** (1/3)
        print(f'A média geométrica é {geo}')
    elif media.lower() == 'b':
        pon = (x + (2 * y) + (3 * z)) / 6
        print(f'A media ponderada é {pon}')
    elif media.lower() == 'c':
        har = (1) / ((1 / x) + (1 / y) + (1 / z))
        print(f'A media harmônica é {har}')
    elif media.lower() == 'd':
        ari = (x + y + z) / 3
        print(f'A media aritmética é {ari}')
else: 
    print('Inválido')