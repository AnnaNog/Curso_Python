peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc} e você está abaixo do peso')

elif 18.5 <= imc <= 24.9:
    print(f'Seu IMC é {imc} e você está saudável')

elif 25 <= imc <= 29.9:
    print(f'Seu IMC é {imc} e você está com peso em excesso')

elif 30 <= imc <= 34.9:
    print(f'Seu IMC é {imc} e você está com obesidade grau I')

elif 35 <= imc <= 39.9:
    print(f'Seu IMC é {imc} e você está com obesidade grau II')

else:
    print(f'Seu IMC é {imc} e você está com obesidade grau III')