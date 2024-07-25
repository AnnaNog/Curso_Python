#Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número. Por exemplo, para o número 3025 temos que: 30 + 25 = 55, 55² = 3025

for numero in range(1000, 10000):
    d1 = numero // 100
    d2 = numero % 100
 
    # Calcula a soma dos dígitos
    soma = d1 + d2
 
    # Calcula o quadrado da soma
    quadrado_soma = soma ** 2

    if quadrado_soma == numero:
        print(f'O número {numero} possui a propriedade')
