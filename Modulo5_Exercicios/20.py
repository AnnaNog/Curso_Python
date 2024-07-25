#Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e os valores pares. O processo termina quando for digitado o número 100

par = 0
lido = 0
num = 0

while num != 100:
    num = int(input('Digite um número: '))
    if num == 100:
        break
    lido = lido + 1
    if num % 2 == 0:
        print(f'O {num} é par')
        par = par + 1
    
print (f'O total de número lidos é {lido} e {par} são pares')