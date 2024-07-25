#Escreva um programa que leia as coordenadas x e y de pontos no R^2 e calcule sua distância da origem (0,0)
import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
dist = math.sqrt(x**2 + y**2)
print(f"A distância da origem é {dist}")
