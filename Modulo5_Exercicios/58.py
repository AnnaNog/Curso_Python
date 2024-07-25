#Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.

a = int(input('Digite a: '))
b = int(input('Digite b: '))

soma = 0

for num in range (a, b+1):
    primo = 1
    if num <= 1:
        primo = 0
    elif num == 2:
        primo = 1
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = 0
                break
    if primo == 1:
        soma = soma + num

print(f'A soma dos numeros primos é {soma}')