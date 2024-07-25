#Leia um temperatura em graus Kevin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K - 273.15
kevin = float(input('Temperatura em Kevin: '))
celcius = kevin - 273.15
print(f'A temperatura em Celcius é {celcius}')