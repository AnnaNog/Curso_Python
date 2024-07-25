#Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A priveira deve usar a estrutura de repetição for, a segunta while, e a terceira do while
for i in range(1, 101):
    print(i) 

i = 1
while i <= 100:
    print(i)
    i = i + 1

i = 1
while True:
    print(i)
    i = i + 1
    if i > 100:
        break 