nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f'A média é {media}')
else:
    print('Insira uma nota valida')