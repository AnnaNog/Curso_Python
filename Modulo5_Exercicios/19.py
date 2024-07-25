#Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o número
num = int(input('Digite um número entre 100 e 999: '))

if 100 <= num <= 999:
    num_s = str(num)
    for digito in num_s:
        print(digito)