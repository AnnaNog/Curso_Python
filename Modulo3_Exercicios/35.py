#Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa=a2+b2. Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação
import math
numero1 = float(input('Insira o lado do triângulo: '))
numero2 = float(input('Insira o outro lado do triângulo: '))
h = math.sqrt((numero1**2)+(numero2**2))
print(f'A hipotenusa é {h}')