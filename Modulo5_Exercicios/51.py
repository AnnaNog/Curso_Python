#Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.

inicial = 2000

aumento = 1.5/100

for ano in range(1996, 2024):
    inicial = inicial + (inicial * aumento)
    aumento *= 2  

print(f"O salário atual é de {inicial:.2f} reais.")

