#Faça um algoritmo que leia um número positivo e imprima seus divisores

numero = int(input("Digite um número positivo: "))

if numero > 0:
    for i in range (1, numero + 1):
        if numero % i == 0:
            print(i)

else:
    print('Insira um número positivo')