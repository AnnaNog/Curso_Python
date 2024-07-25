valor = float(input('Insira o valor desejado: '))
estado = (input('Insira o estado (MG / SP / RJ / MS): '))

if estado.upper() == 'MG':
    imposto = valor * 1.07
    print(f'O preço final para {estado} é {imposto}')
elif estado.upper() == 'SP':
    imposto = valor * 1.12
    print(f'O preço final para {estado} é {imposto}')
elif estado.upper() == 'RJ':
    imposto = valor * 1.15
    print(f'O preço para {estado} é {imposto}')
elif estado.upper() == 'MS':
    imposto = valor * 1.08
    print(f'O preço para {estado} é {imposto}')
else:
    print('Estado inválido')