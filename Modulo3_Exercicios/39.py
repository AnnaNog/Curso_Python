#A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
 
#- O primeiro ganhador receberá 46%;
# - O segundo receberá 32%;
#- O terceiro receberá o restante;
#- Calcule e imprima a quantia ganha por cada um dos ganhadores.

num = 780000.00
primeiro = num * 0.46
segundo = num * 0.32
terceiro = 780000 - (primeiro + segundo)
print(f'O valor do primeiro é {primeiro}, o valor do segundo é {segundo} e o valor do terceiro é {terceiro}')