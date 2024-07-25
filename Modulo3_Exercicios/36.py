#Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V=π∗raio2∗altura, onde π=3.141592
h = float(input('Insira a altura: '))
r = float(input('Insira o raio: '))
vol = 3.141592 * (r**2) * h
print(f'o volume é {vol}')