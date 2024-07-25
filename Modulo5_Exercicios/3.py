#Faça um algoritmo usando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a contagem

num = 10
while num < 11:
    print(num)
    num = num - 1
    if num == -1:
        break 
print('FIM!')