#Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares
real = float(input('Insira o valor em real: '))
cdolar = float(input('Insira a cotação do dólar: '))
dolar = real / cdolar
print(f'O valor em dólar é: {dolar}')