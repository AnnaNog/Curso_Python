#Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda
sal = 30.00
dias = float(input('Insira a quantidade de dias trabalhados: '))
salario = (sal*dias)
valorliq = salario - (salario*0.08)
print(f'O valor líquido é {valorliq}')