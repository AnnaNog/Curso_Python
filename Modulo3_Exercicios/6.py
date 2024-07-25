#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C*(9/5)+32
celcius = float(input('Temperatura em Celcius: '))
fahrenheit = celcius * (9/5) + 32
print(f'A temperatura em Fahrenheit é {fahrenheit}')