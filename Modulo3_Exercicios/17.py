#Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de conversão é P = C/2.54
cm = float(input('Comprimento em cm: '))
pol = cm / 2.54
print(f'Comprimento em polegadas {pol}')