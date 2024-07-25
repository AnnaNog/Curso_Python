#Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não

numero = int(input("Digite um número: "))

primo = 1

if numero <= 1:
    primo = 0
elif numero == 2:
    primo = 1
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = 0
            break

if primo == 1:
    print(f'{numero} é primo')
else: 
    print(f'{numero} não é primo')
