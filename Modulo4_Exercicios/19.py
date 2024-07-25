num = int(input('Digite um numero: '))

if (num % 3 == 0) != (num % 5 == 0):
    print(f'{num} é divisível por 3 ou 5')
else:
    print("Numero inválido")