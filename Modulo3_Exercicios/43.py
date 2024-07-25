#Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
#- o total a pagar com desconto de 10%;
#- o valor de cada parcela, no parcelamento de 3x sem juros;
#- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
#- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input('Insira o valor: '))
des = valor - (valor*0.1)
parc = valor / 3
comi_vista = des * 0.05
comi = valor * 0.05
print(f'O valor com desconto é {des}, parcelado é {parc}, a comissão à vista é {comi_vista} e a comissão no parcelado é {comi}')