#Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Solicita o número inteiro não negativo ao usuário
n = int(input("Digite um número inteiro não negativo: "))

# Calcula a soma dos n primeiros números primos
soma_primos = 0
count = 0
current_number = 2

while count < n:
    if is_prime(current_number):
        soma_primos += current_number
        count += 1
    current_number += 1

# Imprime o resultado
print(f"A soma dos {n} primeiros números primos é: {soma_primos}")


'''n = int(input('Digite um número: '))

soma = 0
soma_primos = 0
numero = 2

while soma_primos < n:
    primo = 1
    if numero <= 1:
        primo = 0
    elif numero == 2:
        primo = 1
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = 0
                break
        
        if primo == 1:
            soma = soma + numero 
            soma_primos = soma_primos + 1

        numero = numero + 1

print(f'a soma dos {n} numeros primos é {soma}')'''