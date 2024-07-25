# Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kWh, e para cada habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor.

num_habitantes = int(input("Digite o número de habitantes da cidade: "))

valor_kwh = float(input("Digite o valor do kWh: "))

consumo_total = 0
maior_consumo = 0
menor_consumo = 1000

total_residencial = 0
total_comercial = 0
total_industrial = 0

for i in range(1, num_habitantes + 1):
    print(f"\nDados do habitante {i}:")
    consumo = float(input("Digite o consumo do mês (em kWh): "))
    codigo_consumidor = int(input("Digite o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial): "))

    if consumo > maior_consumo:
        maior_consumo = consumo
    if consumo < menor_consumo:
        menor_consumo = consumo
    
    consumo_total += consumo
    
    if codigo_consumidor == 1:
        total_residencial += consumo
    elif codigo_consumidor == 2:
        total_comercial += consumo
    elif codigo_consumidor == 3:
        total_industrial += consumo
    else:
        print(f"Erro: Código de consumidor inválido para o habitante {i}.")
        continue

if num_habitantes > 0:
    media_consumo = consumo_total / num_habitantes
else:
    media_consumo = 0

print("\nResultados:")
print(f"Maior consumo: {maior_consumo} kWh")
print(f"Menor consumo: {menor_consumo} kWh")
print(f"Média de consumo: {media_consumo} kWh")

print("\nTotal de consumo por categoria:")
print(f"Residencial: {total_residencial} kWh")
print(f"Comercial: {total_comercial} kWh")
print(f"Industrial: {total_industrial} kWh")

