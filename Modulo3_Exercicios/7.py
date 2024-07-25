#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = 5*(F-32)/9
fahrenheit = float(input('Temperatura em Fahrenheit: '))
celcius = 5 * (fahrenheit - 32)/9
print(f'A temperatura em Celcius é {celcius}')