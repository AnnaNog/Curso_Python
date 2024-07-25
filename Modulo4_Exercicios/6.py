num1 = int(input('Insira um numero: '))
num2 = int(input('Insira outro numero: '))

if num1 > num2:
    dif = num1 - num2
    print(f'O numero {num1} é maior que o {num2} e a diferença dos dois é {dif}')
elif num1 < num2:
    dif = num2 - num1
    print(f'O numero {num2} é maior que o {num1} e a diferença dos dois é {dif}')
else:
    print('Os números são iguais')