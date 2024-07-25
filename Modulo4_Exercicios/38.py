dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

ano_atual = 2008

if mes == (1 or 3 or 5 or 7 or 9 or 11):
    if dia <= 31 and ano <= ano_atual:
        print(f'A data {dia}/{mes}/{ano} é valida')
    else:
        print(f'A data {dia}/{mes}/{ano} não é valida')

elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        if dia <= 29 and ano <= ano_atual:
            print(f'A data {dia}/{mes}/{ano} é valida')
        else:
            print(f'A data {dia}/{mes}/{ano} não é valida')
    else:
        if dia <= 28 and ano <= ano_atual:
            print(f'A data {dia}/{mes}/{ano} é valida')
        else:
            print(f'A data {dia}/{mes}/{ano} não é valida')

else:
    if dia <= 30 and ano <= ano_atual:
        print(f'A data {dia}/{mes}/{ano} é valida')
    else:
        print(f'A data {dia}/{mes}/{ano} não é valida')