#Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões

limite = 2000000
soma = 0

for numero in range(2, limite):
    primo = 1
    if numero <= 1:
        primo = 0
    elif numero == 2:
        primo = 1
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = 0
                break
    
    if primo == 1:
        soma += numero

print(f"A soma de todos os números primos abaixo de dois milhões é: {soma}")
