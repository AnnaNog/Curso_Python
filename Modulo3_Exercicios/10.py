#Leia uma velocidade em km/h e apresente-a convertida em m/s. A fórmula de conversão é m/s = km/h / 3.6
km = float(input('Velocidade em km/h: '))
ms = km / 3.6
print(f'A velocidade em m/s é {ms}')