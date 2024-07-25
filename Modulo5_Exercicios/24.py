#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número com exceção dele prórpio. Ex: se o usuário informar o número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.
numero = int(input("Digite um número: "))
soma = 0

for i in range (1, numero):
    if numero % i == 0:
        soma = soma + i
print(soma)
