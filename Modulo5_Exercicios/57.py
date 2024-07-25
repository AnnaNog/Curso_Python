#Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário

a = int(input('Digite a: '))
b = int(input('Digite b: '))

contador = 0

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
        contador = contador + 1

print(f'A quantidade de numeros primos é {contador}')
