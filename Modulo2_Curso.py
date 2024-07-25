"""
* PEP8 - propostas de melhorias para as linguagens Python

* The Zen of Phyton -> import this

* A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica (visualmente agradável)

* 1 - Utilize Camel Case para nomes de classes:
- Correto:  
    class Calculadora:
        pass
        
    class CalculadoraCientifica:
        pass   
        
- Incorreto:         
    class calculadora_cientifica:
        pass

* 2 - Utilize nomes em minúsculo, separados por underline para funções ou variáveis:
    def soma():
        pass
    
    def soma_dois():
        pass
    
    numero = 4

    numero_impar = 5

* 3 - Utilize 4 espaços para identação!
    if 'a' in 'banana':
        print('tem')

* 4 - Linhas em branco: 
    - Separar funções e deficições de classe com duas linhas em braco
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco

* 5 - Imports:
    - Imports devem ser sempre feitos em linhas separadas
    EX:
    - Errado:
        import sys,os
    -Certo:
        import sys
        import os
* 6 - Espaços em expressões e instruções

* 7 - Termine sempre uma instrução com uma nova linha
"""

"""
* Dir e Help -> utilitários Python para te auxiliar na programação

* dir -> apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável
EX:
    dir(Tipo de dado/variável)
    print(dir('geek'))

* help -> apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável
"""

"""
* Recebendo dados do usuário

    #Exemplo de print 'antigo' 2.x
#Entrada de dados
print("Qual seu nome? ")
nome = input()
#Saída de dados
print('Seja bem-vindo(a) %s' % nome)

print("Qual o seu nome?")
nome = input() # Input é Entrada
print("Seja bem-vindo %s" % nome)
print("Qual a sua idade?")
idade = input()
print("A %s tem %s anos" % (nome, idade))

    #Exemplo de print 'moderno' 3.x
print("Qual o seu nome?")
nome = input() # Input é Entrada

print('Seja bem-vindo(a) {0}'. format(nome))
print("Qual a sua idade?")
idade = input()
print('A {0} tem {1} anos' .format(nome, idade))

    #Exemplo print mais atual
print("Qual o seu nome?")
nome = input() # Input é Entrada
print(f'Seja bem-vindo(a) {nome}')
print("Qual a sua idade?")
idade = input()
print(f'A {nome} tem {idade} anos')

nome = input('Qual seu nome? ')
print(f'Seja bem-vindo(a) {nome}')


* Input -> entrada, todo dado recebido via input é do tipo string
* Cast é a conversão de um tipo de dado para outro
* String é tudo que estiver entre:
    - Aspas simples: 'Angelina'
    - Aspas duplas: "Angelina"
    - Aspas simples triplas: '''Angelina'''
    - Aspas duplas triplas
"""
