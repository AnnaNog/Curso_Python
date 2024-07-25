salario_atual = float(input('Insira o salário atual: '))
tempo_servico = float(input('Insira o tempo de serviço: '))

if salario_atual <= 500.00:
    reajuste = salario_atual * 1.25
    if tempo_servico < 1:
        print(f'Seu salário vai ficar {reajuste}')
    elif 1 <= tempo_servico <= 3:
        salario_novo = reajuste + 100.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 4 <= tempo_servico <= 6:
        salario_novo = reajuste + 200.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 7 <= tempo_servico <= 10:
        salario_novo = reajuste + 300.00
        print(f'Seu salário vai ficar {salario_novo}')
    else:
        salario_novo = reajuste + 500.00
        print(f'Seu salário vai ficar {salario_novo}')

elif 500.00 < salario_atual <= 1000.00:
    reajuste = salario_atual * 1.20
    if tempo_servico < 1:
        print(f'Seu salário vai ficar {reajuste}')
    elif 1 <= tempo_servico <= 3:
        salario_novo = reajuste + 100.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 4 <= tempo_servico <= 6:
        salario_novo = reajuste + 200.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 7 <= tempo_servico <= 10:
        salario_novo = reajuste + 300.00
        print(f'Seu salário vai ficar {salario_novo}')
    else:
        salario_novo = reajuste + 500.00
        print(f'Seu salário vai ficar {salario_novo}')

elif 1000.00 < salario_atual <= 1500.00:
    reajuste = salario_atual * 1.15
    if tempo_servico < 1:
        print(f'Seu salário vai ficar {reajuste}')
    elif 1 <= tempo_servico <= 3:
        salario_novo = reajuste + 100.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 4 <= tempo_servico <= 6:
        salario_novo = reajuste + 200.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 7 <= tempo_servico <= 10:
        salario_novo = reajuste + 300.00
        print(f'Seu salário vai ficar {salario_novo}')
    else:
        salario_novo = reajuste + 500.00
        print(f'Seu salário vai ficar {salario_novo}')

elif 1500.00 < salario_atual <= 2000.00:
    reajuste = salario_atual * 1.10
    if tempo_servico < 1:
        print(f'Seu salário vai ficar {reajuste}')
    elif 1 <= tempo_servico <= 3:
        salario_novo = reajuste + 100.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 4 <= tempo_servico <= 6:
        salario_novo = reajuste + 200.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 7 <= tempo_servico <= 10:
        salario_novo = reajuste + 300.00
        print(f'Seu salário vai ficar {salario_novo}')
    else:
        salario_novo = reajuste + 500.00
        print(f'Seu salário vai ficar {salario_novo}')

else:
    if tempo_servico < 1:
        print(f'Seu salário vai ficar {salario_atual}')
    elif 1 <= tempo_servico <= 3:
        salario_novo = salario_atual + 100.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 4 <= tempo_servico <= 6:
        salario_novo = salario_atual + 200.00
        print(f'Seu salário vai ficar {salario_novo}')
    elif 7 <= tempo_servico <= 10:
        salario_novo = salario_atual + 300.00
        print(f'Seu salário vai ficar {salario_novo}')
    else:
        salario_novo = salario_atual + 500.00
        print(f'Seu salário vai ficar {salario_novo}')