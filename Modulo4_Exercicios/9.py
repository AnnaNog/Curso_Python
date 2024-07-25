sal = float(input('Insira o salário: '))
emp = float(input('Insira o valor da prestação do empréstimo: '))

if emp > 0.2 * sal:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')