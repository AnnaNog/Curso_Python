preco_antigo = float(input('Insira o preço antigo: '))

if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05
    if preco_novo <= 80:
        print(f'O preço novo é {preco_novo} e o produto está barato')
    elif 80 < preco_novo <= 120:
        print(f'O preço novo é {preco_novo} e o produto está normal')
    elif 120 < preco_novo <= 200:
        print(f'O preço novo é {preco_novo} e o produto está caro')
    else:
        print(f'O preço novo é {preco_novo} e o produto está muito caro')

elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.1
    if preco_novo <= 80:
        print(f'O preço novo é {preco_novo} e o produto está barato')
    elif 80 < preco_novo <= 120:
        print(f'O preço novo é {preco_novo} e o produto está normal')
    elif 120 < preco_novo <= 200:
        print(f'O preço novo é {preco_novo} e o produto está caro')
    else:
        print(f'O preço novo é {preco_novo} e o produto está muito caro')

else:
    preco_novo = preco_antigo * 1.15
    if preco_novo <= 80:
        print(f'O preço novo é {preco_novo} e o produto está barato')
    elif 80 < preco_novo <= 120:
        print(f'O preço novo é {preco_novo} e o produto está normal')
    elif 120 < preco_novo <= 200:
        print(f'O preço novo é {preco_novo} e o produto está caro')
    else:
        print(f'O preço novo é {preco_novo} e o produto está muito caro')