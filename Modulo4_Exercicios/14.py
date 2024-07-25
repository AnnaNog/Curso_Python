nota1 = float(input('Insira a nota de trabalho: '))
nota2 = float(input('Insira a nota da avaliação: '))
nota3 = float(input('Insira a nota do exame: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10 
    if 0<= media <= 2.9:
        print('Reprovado')
    elif 3<= media <=4.9:
        print('Recuperação')
    else:
        print('Aprovado')