#Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo
escada = float(input('Insira a altura do degrau: '))
valor = float(input('Insira a altura desejada: '))
quant = valor / escada
print(f'A quantidade de degraus que você deve subir é {quant}')