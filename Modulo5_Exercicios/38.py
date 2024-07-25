#Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000. Um terno pitagórico é um conjunto de três números naturais, a, b, c, para o qual,
#a^2+b^2=c^2

soma = 1000

for a in range(1, soma):
    for b in range(a, soma):
        c = soma - a - b
        if a**2 + b ** 2 == c **2:
            print(f'O termo é a = {a}, b = {b} e c = {c}')