#Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base
base = float(input('Insira o salário base: '))
gra = base*0.05
des = base*0.07
valorfin = base + gra - des
print(f'O valor final é {valorfin}')