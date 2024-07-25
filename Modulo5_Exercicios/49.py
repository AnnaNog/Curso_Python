#O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas

carlos = 1
joao = 1 / 3

meses = 0
while joao < carlos:
    carlos =carlos * 1.02  
    joao = joao * 1.05    
    meses = meses + 1

print(f"Quantidade de meses: {meses}")
