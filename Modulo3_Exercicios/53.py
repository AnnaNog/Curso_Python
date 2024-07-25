#Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela
comprimento = float(input("Comprimento do terreno: "))
largura = float(input("Largura do terreno: "))
preco_m = float(input("Preço do metro : "))

area = (comprimento*2) + (largura * 2)
preco = (area * preco_m)

print(f"O custo seria {preco}")