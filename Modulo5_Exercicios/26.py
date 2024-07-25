#Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado 

num = int(input('Insira um número: '))

num2 = num + 1

while num2 % 11 != 0 and num2 % 13 != 0 and num2 % 17 != 0:
    num2 = num2 + 1

print (num2)