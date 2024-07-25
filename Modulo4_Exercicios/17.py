basem = float(input('Insira a base maior: '))
base = float(input('Insira a base menor: '))
altura = float(input('Insira a altura: '))

if basem > 0 and base > 0:
    area = ((basem + base) * altura) / 2 
    print(f'A área do trapézio é {area}')
else:
    print('Inválido')