"""
Condicionais -> if, else e elif

* Deixa o programa mais esperto, dando caminhos diferentes para resolver problemas

* IF (se)
    - EX:
        idade = 6
        if idade < 18:
            print('Menor de idade')

* ELSE (senão)
    - EX:
        idade = 26
        if idade < 18:
            print('Menor de idade')
        else:
            print('Maior de idade')

* ELIF (else if / senão)
    - EX:
        idade = 15
        if idade < 18:
            print('Menor de idade')
        elif idade == 18:
            print('Tem 18 anos')
        else:
            print('Maior de idade')
"""

"""
* Estruturas lógicas -> And, or, not, is

* Operadores unários:
    - not

* Operadores binários:
    - and, or, is

* AND (e) -> ambos os valores precisam ser True
    - EX:
        ativo = True
        logado = True
        if ativo and logado:
            print('Bem-vindo usuário')
        else:
            print('Você precisa ativar a sua conta')

* OR (ou) -> um ou outro valor precisa ser True
    - EX: 
        ativo = True
        logado = False
        if ativo or logado:
            print('Bem-vindo usuário')
        else:
            print('Você precisa ativar a sua conta')

* NOT -> o valor do booleano é invertido, se for True vira False, se for False vira True
    - EX:
        ativo = False
        logado = False
        if not ativo:
            print('Você precisa ativar a sua conta')
        else:
            print('Bem-vindo usuário') 

* IS 
    - EX: 
        ativo = True
        logado = False
        if ativo is False:
            print('Você precisa ativar a sua conta')
        else:
            print('Bem-vindo usuário')
"""