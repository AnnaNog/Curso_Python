operacoes = float(input('Escolha a operação desejada: 1 - Soma de dois números \n 2 - Diferença entre dois números \n 3 - Produto entre dois números \n 4 - Divisão entre dois números '))
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

if operacoes == 1:
    soma = num1 + num2 
    print(f'A soma é {soma}')
elif operacoes == 2:
    if num1 > num2:
        sub = num1 - num2 
        print(f'A subtração é {sub}')
    else:
        sub = num2 - num1
        print(f'A subtração é {sub}')
elif operacoes == 3:
    mul = num1 * num2 
    print(f'A multiplicação é {mul}')
elif operacoes == 4:
    if num2 != 0:
        div = num1 / num2 
        print(f'A divisão é {div}')
    else:
        print('A divisão não pode ser realizada')
else:
    print("Número inválido")