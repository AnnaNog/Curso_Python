km = float(input('Insira a quantidade de km: '))
l = float(input('Insira quantos litros foram gastos: '))

kml = km / l

if kml < 8:
    print(f'Venda o carro seu consumo é de {kml} km/l')
elif 8 <= kml <=12:
    print(f'Econômico seu consumo é de {kml} km/l')
else: 
    print(f'Super Econômico seu consumo é de {kml} km/l')