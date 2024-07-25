num1 = float(input('Insira o numero 1: '))
num2 = float(input('Insira o numero 2: '))
num3 = float(input('Insira o numero 3: '))

if num1 <= num2 <= num3:
    print(f"Números em ordem crescente: {num1}, {num2}, {num3}")
elif num1 <= num3 <= num2:
    print(f"Números em ordem crescente: {num1}, {num3}, {num2}")
elif num2 <= num1 <= num3:
    print(f"Números em ordem crescente: {num2}, {num1}, {num3}")
elif num2 <= num3 <= num1:
    print(f"Números em ordem crescente: {num2}, {num3}, {num1}")
elif num3 <= num1 <= num2:
    print(f"Números em ordem crescente: {num3}, {num1}, {num2}")
else:
    print(f"Números em ordem crescente: {num3}, {num2}, {num1}")