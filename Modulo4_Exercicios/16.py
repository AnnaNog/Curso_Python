numero = int(input("Digite um número entre 1 e 12: "))

meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
 }

if 1 <= numero <= 12:
        print (meses[numero])
else:
        print('numero invalido')