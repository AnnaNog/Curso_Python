#Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real

valor_saque = int(input("Digite o valor do saque: "))

quantidade_100 = 0
quantidade_50 = 0
quantidade_20 = 0
quantidade_10 = 0
quantidade_5 = 0
quantidade_2 = 0
quantidade_1 = 0

while valor_saque >= 100:
    quantidade_100 = quantidade_100 + 1
    valor_saque = valor_saque - 100

while valor_saque >= 50:
    quantidade_50 = quantidade_50 + 1
    valor_saque = valor_saque - 50

while valor_saque >= 20:
    quantidade_20 = quantidade_20 + 1
    valor_saque = valor_saque - 20

while valor_saque >= 10:
    quantidade_10 = quantidade_10 + 1
    valor_saque = valor_saque - 10

while valor_saque >= 5:
    quantidade_5 = quantidade_5 + 1
    valor_saque = valor_saque - 5

while valor_saque >= 2:
    quantidade_2 = quantidade_2 + 1
    valor_saque = valor_saque - 2

quantidade_1 = valor_saque

# Imprime o resultado
print("Quantidade de notas:")
print(f"{quantidade_100} nota(s) de 100 reais")
print(f"{quantidade_50} nota(s) de 50 reais")
print(f"{quantidade_20} nota(s) de 20 reais")
print(f"{quantidade_10} nota(s) de 10 reais")
print(f"{quantidade_5} nota(s) de 5 reais")
print(f"{quantidade_2} nota(s) de 2 reais")
print(f"{quantidade_1} nota(s) de 1 real")

