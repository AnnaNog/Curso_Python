#Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico

chico = 1.50
ze = 1.10

crescimento_chico = 2
crescimento_ze = 3

anos = 0

while ze <= chico:
    anos = anos + 1
    
    chico = chico + crescimento_chico / 100
    ze = ze + crescimento_ze / 100

print(f"Serão necessários {anos} anos")
