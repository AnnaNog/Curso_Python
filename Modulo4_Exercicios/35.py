dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

if mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    if dia <= 31:
        print(f'A data {dia}/{mes}/{ano} é valida')
    else:
        print(f'A data {dia}/{mes}/{ano} não é valida')

elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        if dia <= 29:
            print(f'A data {dia}/{mes}/{ano} é valida')
        else:
            print(f'A data {dia}/{mes}/{ano} não é valida')
    else:
        if dia <= 28:
            print(f'A data {dia}/{mes}/{ano} é valida')
        else:
            print(f'A data {dia}/{mes}/{ano} não é valida')

else:
    if dia <= 30:
        print(f'A data {dia}/{mes}/{ano} é valida')
    else:
        print(f'A data {dia}/{mes}/{ano} não é valida')