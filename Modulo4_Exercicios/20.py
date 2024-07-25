lado1 = float(input('Insira um lado: '))
lado2 = float(input('Insira o segundo lado: '))
lado3 = float(input('Insira o terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isosceles')
    else: 
        print('O triângulo é escaleno')
else:
    print('Os valores não correspondem a um triângulo')