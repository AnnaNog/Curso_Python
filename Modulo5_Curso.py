"""
Loop for - 

Loop -> estrutura de repetição

For -> uma dessas estruturas

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
 - String
    nome = 'Geek'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

#Exemplo de for 1 (iterando em uma string)

for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1,10):
    print(numero)

range(valor_inicial, valor_final)
OBS: O valor final não é inclusive

Enumerate:
((0, 'G'), (1, 'e'))....

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: quando não precisamos de um valor podemos descarta-lo utilizando um _

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar'))
  
for n in range(1, qtd+1):
    print(f'Imprimindo{n}') 

qtd = int(input('Quantas vezes esse loop deve rodar'))
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'Informe o {n}/{qtd} valor: ')) 
    soma = soma + numero
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Unicode -> imprimir emoji
- Original: U+1F60D
- Modificado: U0001F60D

for num in range(1,11):
    print('\U0001F60D' * num)
"""     

"""
Entendendo e explorando ranges - 

- Precisamos conhecer o loop for para usar os ranges

- Precisamos conhecer o renge para trabalhar melhor com loops for

- Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada

- Formas gerais:
range(valor_de_parada)

#Forma 1
for num in range(11):
    print(num)

#Forma 2
range(valor_de_inicio, valor_de_parada)
for num in range(4,12):
    print(num)

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)
for num in range(1,10,2):
    print(num)

#Forma 4 (inversa)
range(valor_inicio, valor_de_parada, passo)
for num in range(10,0, -1) :
    print(num)
"""

"""
Loop while - 

- Forma geral

while expressão_booleana:
    //execução do loop

- O bloco do while será repetido enquanto a expressão booleana for verdadeira

- Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

- Exemplo:

num = 5
num < 5

num = 1
while num < 10:
    print(num)
    num = num + 1

OBS: Em um loop while é importante que cuidemos do critério de parada

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou? ')
"""

"""
Saindo de loops com break -

- Funciona da mesma forma que nas linguagens C e java

- Utilizamos o break para sair de loops de maneira projetada

for num in range(1,11):
    if num == 6:
        break
    else: print(num)

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
"""
