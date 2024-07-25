idade = int(input('Digite a sua idade: '))
tempo = int(input('Digite seu tempo de serviço: '))

if idade >= 65:
    print('Pode se aposentar')
elif tempo >= 30:
    print('Pode se aposentar')
elif idade >= 60 and tempo >= 25:
    print('Pode se aposentar')
else:
    print("Não pode se aposentar")