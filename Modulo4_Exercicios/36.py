venda = float(input('Insira o valor da venda: '))

if venda >= 100000:
    comissao = 700 + (venda * 0.16)
    print(f'A comissão é de {comissao}')

elif 100000 > venda >= 80000:
    comissao = 650 + (venda * 0.14)
    print(f'A comissão é de {comissao}')

elif 80000 > venda >= 60000:
    comissao = 600 + (venda * 0.14)
    print(f'A comissão é de {comissao}')

elif 60000 > venda >= 40000:
    comissao = 550 + (venda * 0.14)
    print(f'A comissão é de {comissao}')

elif 40000 > venda >= 20000:
    comissao = 500 + (venda * 0.14)
    print(f'A comissão é de {comissao}')

else:
    comissao = 400 + (venda * 0.14)
    print(f'A comissão é de {comissao}')