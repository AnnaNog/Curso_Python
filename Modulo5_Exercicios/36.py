#Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais é,
#1^2+2^2+...+10^2=385
#O quadrado da soma dos dez primeiros números naturais é,
#(1+2+...+10)^2=55^2=3025
#A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é
#3025−385=2640

passo_um = 0
dois = 0

for i in range(1,101):
    passo_um = passo_um + (i ** 2)
    dois = dois + i
    passo_dois = dois ** 2

passo_tres = passo_dois - passo_um
print(f'O passo 1 é {passo_um}, o passo 2 é {passo_dois} e a diferença é {passo_tres}')