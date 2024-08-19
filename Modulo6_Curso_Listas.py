'''
Listas:
- Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinâmicos e podermos colocar QUALQUER tipo de dado
- Linguagens C/Java:
    - Possuem tamanho e tipo fixo, ou seja, nessas linguagens se você criar um array do tipo int com tamanho 5, este array será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores
- Em Python: 
    - Dinâmico: não possui tamanho fixo, ou seja podemos criar a lista e simplesmente ir adicionando elementos
    - Qualquer tipo de dado: as listas não possuem tipo de dado fixo ou seja podemos colocar qualquer tipo de dado
    - As listas em python são representadas por []
    - EX:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e','k']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

if 8 in lista4:
    print('Encontrei o número 8')

else:
    print('Não encontrei o número 8')
    - Podemos facilmente checar se determinado valor está contido na lista
    - Podemos facilmente ordernar uma lista -> nome.sort()
    - Podemos facilmente contar o número de ocorrencias de um valor em um lista -> print(nome.count('e'))
    - Para adicionar utilizamos a função nome.append() -> com a função só conseguimos adicionar um elemento por vez
    - nome.append([8, 3, 1])-> lista dentro de outra lista
    - nome.extend([23, 32, 43])-> colocacada elemento da lista como um valor adicional à lista
    - Podemos inserir um novo elemnto na lista informando a posição do índice -> nome.inser(2, 'Novo Valor')
    - Podemos facilmente juntar duas listas -> lista6 = lista1 + lista2
        - Sem criar uma nova lista -> lista1.extend(lista2)

lista.reverse() -> inverte a lista

print(lista1[::-1]) -> inverte a lista 

lista6 = lista2.copy() -> copia uma lista

print(len(lista3)) -> tamanho da lista

- Podemos facilmente remover o último elemento de uma lista
    lista5.pop()
    print(lista5)

- Remover elemento pelo índice
    lista5.pop(2)
    print(lista5)

- Podemos remover todos os elementos
    lista5.clear()
    print(lista5)

- Podemos facilmente repetir elementos em uma lista
    nova = [1, 2, 3]
    nova = nova * 3

- Podemos facilmente converter uma string para uma lista
OBS: por padrão o split separa os elementos da lista pelo espaço entre elas
    - Exemplo 1
        curso = 'Programação em Python'
        print(curso)
        curso = curso.split()
        print(curso)

    - Exemplo 2
        curso = 'Programação,em,Python'
        print(curso)
        curso = curso.split(',')
        print(curso)

- Convertendo uma lista em uma string
    lista6 =  ['Programação', 'em', 'Python']
    print(lista6)
    curso = ' '.join(lista6)
    print(lista6)

- Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
    lista6 = [1, 2, True, 'Geek, 'd', [1,2,3], 43546463562462]

- Iterando sobre listas
    - Exemplo 1 -> for
        for elemento in lista1:
            print(elemento)
            soma = soma + elemento
        print(soma)

    - Exemplo 2 -> while
        carrinho = []
        produto = ''

        while produto != 'sair'
            print("Adicione um produto na lista ou digite 'sair' para sair: ")
            produto = input()
            if proguto !=  'sair': 
                carrinho.append(produto)
        for produto in carrinho:
            print(produto)

- Utilizando variáveis em listas
    num = [1, 2, 3, 4, 5]

    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    num5 = 5

    num = [num1, num2, num3, num4, num5]

- Fazemos acesso aos elementos de forma indexada
    cores = ['verde', 'amarelo', 'azul', 'branco']

    print(cores[0])

- Fazer acesso aos elementos de forma indexada inversa
    print(cores[-1])

- Loop
    for cor in cores:
        print(cor)

    indice = 0
    while indice < len(cores):
        print(cores[indice])
        indice = indice + 1

- Gerar índice em um for
    for indice, cor in enumerate(cores):
        print(indice, cor)

- Outros métodos não tão importantes mas úteis

- Encontrar o índice de um elemento na lista
    numeros = [5, 6, 7, 8, 9]
    print(numeros.index(6))

- Podemos fazer busca dentro de um range, ou seja, qual indíce começar
    print(numeros.index(5, 1))

- Podemos fazer busca dentro de um range, início/fim
    print(numeros.index(8, 3, 6)) -> buscar valor 8 entre o índice 3 e 6

- Revisão slicing
    lista[inicio:fim:passo]
    range[inicio:fim:passo]

- Trabalhando com slice de lista com o parâmetro 'inicio'
    lista = [1, 2, 3, 4]
    print(lista[1:]) -> iniciando no índice 1 e pegando todos os elementos restantes
    print(lista[::]) -> todos os elementos

- Trabalhando com slice de lista com o parâmetro 'fim'
    lista = [1, 2, 3, 4]
    print(lista[:2]) -> começa em 0 e pega até o índice 2 - 1
    print(lista[:4]) -> começa em 0 e pega até o 4 - 1

- Trabalhando com slice de lista com o parâmetro 'passo'
    lista = [1, 2, 3, 4]
    print(lista[1::2]) -> começa em 1, vai até o final de 2 em 2
    print(lista[::2]) -> começa em 0, vai até o final de 2 em 2

- Invertendo valores em uma lista
    nomes = ['Geek', 'University']
    nomes[0], nomes[1] = nomes[1], nomes[0]
    print(nomes)

    ou 

    nomes = ['Geek', 'University']
    nomes.reverse()
    print(nomes)

- Soma, valor máx, valor min, tamanho -> se os valores forem todos inteiros ou reais (só o tamnho que não)
    lista = [1, 2, 3, 4, 5, 6]
    print(sum(lista))
    print(max(lista))
    print(min(lista))
    print(len(lista))

- Transformar uma lista em tupla
    lista = [1, 2, 3, 4, 5, 6]
    print(lista)
    print(type(lista))

    tupla = tuple(lista)
    print(tupla)
    print(type(lista))

- Desempacotamento de listas
    lista = [1, 2, 3]
    num1, num2, num3 = lista
    print(num1)
    print(num2)
    print(num3)

- Copiando uma lista para outra (Shallow Copy e Deep Copy)
    - Forma 1 - Deep Copy
    lista = [1, 2, 3]
    print(lista)

    nova = lista.copy()
    print(nova)

    nova.append(4)
    print(lista)
    print(nova)

    - Forma 2 - Shallow Copy
    lista = [1, 2, 3]
    print(lista)

    nova = lista
    print(nova)

    nova.append(4)
    print(lista)
    print(nova)
    '''