#Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado
vhoras = float(input('Insira o valor da hora de trabalho: '))
horas = float(input('Insira a quantidade de horas trabalhado: '))
salario = (vhoras*horas)
valorfin = salario + (salario*0.1)
print(f'O valor final é {valorfin}')