codigo = int(input('Insira o código do produto: '))
quant = int(input('Insira a quantidade: '))

if codigo == 100:
    prod = 'Cachorro Quente'
    preco = 1.20
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 101:
    prod = 'Bauru Simples'
    preco = 1.30
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 102:
    prod = 'Bauru com Ovo'
    preco = 1.50
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 103:
    prod = 'Hamburguer'
    preco = 1.20
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 104:
    prod = 'Cheeseburguer'
    preco = 1.70
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 105:
    prod = 'Suco'
    preco = 2.20
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

elif codigo == 106:
    prod = 'Refrigerante'
    preco = 1.00
    valor = preco * quant
    print(f'Foram consumido(s) {quant} do produto {prod} e o valor total é {valor}')

else:
    print('Código inválido')