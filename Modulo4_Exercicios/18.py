operacoes = float(input('Escolha a operação desejada: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão '))
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

if operacoes == 1:
    soma = num1 + num2 
    print(f'A soma é {soma}')
elif operacoes == 2:
    sub = num1 - num2 
    print(f'A subtração é {sub}')
elif operacoes == 3:
    mul = num1 * num2 
    print(f'A multiplicação é {mul}')
elif operacoes == 4:
    div = num1 / num2 
    print(f'A divisão é {div}')
else:
    print("Número inválido")