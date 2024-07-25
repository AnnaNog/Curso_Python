# Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado final, a correspondente média aritmética. O número de notas com que o aluno pretende calcular a média não será fornecido ao programa: o cálculo da média terminará quando for introduzido um valor que não seja válido como nota de aprovação

soma_nota = 0
contagem = 0

nota = float(input('Digite uma nota: '))

while 10 <= nota <= 20:
    contagem = contagem + 1
    soma_nota = soma_nota + nota
    nota = float(input('Digite uma nota: '))

media = soma_nota / contagem
print (f'A média é {media}')
    

