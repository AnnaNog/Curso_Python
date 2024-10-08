# Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores inválido” e o programa termina. Exemplo de tela de saída: Digite o valor inicial e valor final: 5 10 Soma dos ímpares neste intervalo: 21

# Solicita ao usuário os valores inicial e final do intervalo
inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

if inicial > final:
    print("Intervalo de valores inválido")
else:
    impares = 0

    for num in range(inicial, final + 1):
        if num % 2 != 0:
            impares = impares + num

    print(f"Soma dos ímpares neste intervalo: {impares}")
