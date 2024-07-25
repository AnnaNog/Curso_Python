#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido
amigo1 = float(input("Investimento do amigo 1: "))
amigo2 = float(input("Investimento do amigo 2: "))
amigo3 = float(input("Investimento do amigo 3: "))

premio_total = float(input("Valor total do prêmio: "))


investimento_total = amigo1 + amigo2 + amigo3

prop1 = amigo1/investimento_total
prop2 = amigo2/investimento_total
prop3 = amigo3/investimento_total


premio1 = prop1 * premio_total
premio2 = prop2 * premio_total
premio3 = prop3 * premio_total


print(f"Amigo 1 ganharia: R${premio1}")
print(f"Amigo 2 ganharia: R${premio2}")
print(f"Amigo 3 ganharia: R${premio3}")
