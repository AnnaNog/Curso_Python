# Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.

import random

num = random.randint(1, 1000)

tentativas = 0
acertou = 0

while acertou != 1:
    chute = int(input('Tente adivinhar o número: '))
    tentativas = tentativas + 1
    if chute == num:
        acertou = 1
        print(f'Parabéns você acertou o número em {tentativas} tentativas')
    elif chute < num:
        print('O número é maior')
    else: 
        print('O número é menor')