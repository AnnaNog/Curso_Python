# Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice-versa. Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar for escolhida.
opcao = 0

while opcao != 3:
    opcao = int(input('Digite a opção desejada - 1: km/h p/ m/s; 2: m/s p/ km/h; 3: finalizar - '))
    if opcao == 1:
        km = float(input('Digite a velocidade em km/h: '))
        ms = km / 3.6
        print(f'A velocidade em m/s é {ms}')
    elif opcao == 2:
        ms = float(input('Digite a velocidade em m/s: '))
        km = ms * 3.6
        print(f'A velocidade em km/h é {km}')
