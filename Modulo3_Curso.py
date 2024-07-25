"""
* Tipo float

* Tipo real, decimal
* Casas decimais
* Separador de casas decimais na programação é o . e não a ,

- É possível fazer dupla atribuição:
    valor1, valor2 = 1, 44
    print(valor1)
    print(valor2)

- Podemos converter um float para um int
    valor = 1.44
    res = int(valor)
    print(res)

- Podemos trabalhar com números complexos
    atribuir o j na variável

"""

"""
* Tipo booleano

* Álgebra booleana, criada por George Boole
* 2 constantes, verdadeiro ou falso
* True -> Verdadeiro
* False -> Falso
* Sempre com a inicial maiúscula
    ativo = True
    print(ativo)

* Operações básicas:
    - Negação: not (fazendo a negação se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado será verdadeiro)
        ativo = True
        print(ativo)
        print(not ativo)
    - Ou: or (é uma operação binária ou seja depende de dois valores. Ou um ou outro deve ser verdadeiro)
        True or True -> True
        True or False -> True
        False or True -> True
        False or False -> False
            ativo = True
            print(ativo)
            print(not ativo)
            logado = False
            print(ativo or logado)
    - E: and (também é uma operação binária, ou seja, depende de dois valores. Ambos devem ser verdadeiros)
        True and True -> True
        True and False -> False
        False and True -> False
        False and False -> False
            ativo = False
            logado = False
            print(ativo and logado)
"""

"""
* Tipo string

* Em Python, um dado é considerado do tipo string sempre que:
    - Estiver entre aspas simples: ''
    - Estiver entre aspas duplas: ""
    - Estiver entre aspas simples triplas: ''''''
    - Estiver entre aspas duplas triplas
        nome = 'Anna'
        print(nome)
        print(type(nome))
* \n pula linha
* print(nome.upper())
* print(nome.lower())
* print(nome.split()) -> transforma em uma lista de strings
* print(nome[0:4]) -> slice de string, pega sempre um antes no final
* print(nome.splite()[0])
* print(nome[::-1]) -> lê tudo e inverte
* print(nome.replace{'G', 'P'})
"""

"""
* Escopo de variáveis

* 1- Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa
        numero = 42
        print(numero)
* 2- Variáveis locais:
    - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada
        numero = 42
        if numero > 10:
            novo = numero + 10
            print(novo)
"""

