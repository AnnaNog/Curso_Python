#Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i e ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
n = int(input('Digite quantos multiplos: '))
i = int(input('Digite um número: '))
j = int(input('Digite um número: '))

contador = 0
num = 0

if j > 0 and i > 0:
    while contador < n:
        if num % i == 0 or num % j == 0:
            if contador < n - 1:
                print(num, end=', ')
            else:
                print(num)
            contador = contador + 1
        num = num + 1
else:
    print('Os números são negativos')