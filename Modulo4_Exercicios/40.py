custo_fabrica = float(input('Digite o custo de fábrica: '))

if custo_fabrica <= 12000.00:
    distribuidor = custo_fabrica * 0.05
    total = custo_fabrica + distribuidor
    print(f'O custo do consumidor é {total}')

elif 12000 < custo_fabrica <= 25000:
    distribuidor = custo_fabrica * 0.10
    imposto = custo_fabrica * 0.15
    total = custo_fabrica + distribuidor + imposto
    print(f'O custo do consumidor é {total}')

else:
    distribuidor = custo_fabrica * 0.15
    imposto = custo_fabrica * 0.20
    total = custo_fabrica + distribuidor + imposto
    print(f'O custo do consumidor é {total}')