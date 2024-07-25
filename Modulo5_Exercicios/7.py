#Faça um programa que leia 10 inteiros positivos, ignorando não positivos e imprima sua média


total = 0
conta = 0


for i in range(10):
    num = int(input("Digite um número inteiro positivo: "))
    while num <= 0:
        num = int(input("Digite um número inteiro positivo: "))
        
    total = total + num
    conta = conta + 1


    if conta > 9:
        media = total / conta
        print(f"A média dos números positivos é: {media}")

