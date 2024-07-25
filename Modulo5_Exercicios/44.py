# Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.

num = int(input('Digite um número: '))

if num <= 0:
    print('Número inválido')
else:
    anterior = 0
    atual = 1
    print(anterior)
    print(atual)
    while atual <= num:
        prox = anterior + atual
        print(prox)
        anterior = atual
        atual = prox