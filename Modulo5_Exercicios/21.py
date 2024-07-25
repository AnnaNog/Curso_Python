#Faça um programa que receba dois números. Calcule e mostre:

#a soma dos números pares desse intervalo de números, incluindo os números digitados;
#a multiplicação dos números ímpares desse intervalo de números.

num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
par = 0
impar = 1

for i in range(num, num2 + 1):
    if i % 2 == 0:
        par = par + i
    else:
        impar = impar * i

print(f'A soma dos pares é {par} e a multiplicação dos ímpares é {impar}')