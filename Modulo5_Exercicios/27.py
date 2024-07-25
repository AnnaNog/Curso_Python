#Em Matemática, número harmônico designado por H(n) define-se como sendo a soma da série harmônica:

# H(n)=1 + 1/2 + 1/3 ​+...+h/n​

#Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).

n = int(input('Insira um número: '))

h = 0 

if n >= 0:
    for i in range(1, n + 1):
        divisao = 1 / i
        h = h + divisao
print (h)