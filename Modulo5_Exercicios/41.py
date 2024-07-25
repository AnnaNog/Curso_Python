# Faça um programa que calcule a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual a zero.
# R=R1.R2/R1+R2​

r1 = float(input('Digite o R1: '))

while r1 != 0:
    r2 = float(input('Digite o R2: '))
    if r2 == 0:
        break
    r = (r1 * r2) / (r1 + r2)
    print(f'A resistencia é {r}')
    r1 = float(input('Digite o R1: '))