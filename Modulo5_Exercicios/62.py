#Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há 2 + 4 + 4 + 6 + 5 = 22 letras usadas no total. Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil) fossem escritos em palavras. OBS: Não conte espaços ou hífens.
total_letras = 0

for numero in range(1, 1001):
    if numero == 0:
        palavra = ""
    elif numero == 1:
        palavra = "um"
    elif numero == 2:
        palavra = "dois"
    elif numero == 3:
        palavra = "três"
    elif numero == 4:
        palavra = "quatro"
    elif numero == 5:
        palavra = "cinco"
    elif numero == 6:
        palavra = "seis"
    elif numero == 7:
        palavra = "sete"
    elif numero == 8:
        palavra = "oito"
    elif numero == 9:
        palavra = "nove"
    elif numero == 10:
        palavra = "dez"
    elif numero == 11:
        palavra = "onze"
    elif numero == 12:
        palavra = "doze"
    elif numero == 13:
        palavra = "treze"
    elif numero == 14:
        palavra = "quatorze"
    elif numero == 15:
        palavra = "quinze"
    elif numero == 16:
        palavra = "dezesseis"
    elif numero == 17:
        palavra = "dezessete"
    elif numero == 18:
        palavra = "dezoito"
    elif numero == 19:
        palavra = "dezenove"
    elif numero == 20:
        palavra = "vinte"
    elif numero < 30:
        palavra = "vinte e " + palavra
    elif numero == 30:
        palavra = "trinta"
    elif numero < 40:
        palavra = "trinta e " + palavra
    elif numero == 40:
        palavra = "quarenta"
    elif numero < 50:
        palavra = "quarenta e " + palavra
    elif numero == 50:
        palavra = "cinquenta"
    elif numero < 60:
        palavra = "cinquenta e " + palavra
    elif numero == 60:
        palavra = "sessenta"
    elif numero < 70:
        palavra = "sessenta e " + palavra
    elif numero == 70:
        palavra = "setenta"
    elif numero < 80:
        palavra = "setenta e " + palavra
    elif numero == 80:
        palavra = "oitenta"
    elif numero < 90:
        palavra = "oitenta e " + palavra
    elif numero == 90:
        palavra = "noventa"
    elif numero < 100:
        palavra = "noventa e " + palavra
    elif numero == 100:
        palavra = "cem"
    elif numero < 200:
        palavra = "cento e " + palavra
    elif numero == 200:
        palavra = "duzentos"
    elif numero < 300:
        palavra = "duzentos e " + palavra
    elif numero == 300:
        palavra = "trezentos"
    elif numero < 400:
        palavra = "trezentos e " + palavra
    elif numero == 400:
        palavra = "quatrocentos"
    elif numero < 500:
        palavra = "quatrocentos e " + palavra
    elif numero == 500:
        palavra = "quinhentos"
    elif numero < 600:
        palavra = "quinhentos e " + palavra
    elif numero == 600:
        palavra = "seiscentos"
    elif numero < 700:
        palavra = "seiscentos e " + palavra
    elif numero == 700:
        palavra = "setecentos"
    elif numero < 800:
        palavra = "setecentos e " + palavra
    elif numero == 800:
        palavra = "oitocentos"
    elif numero < 900:
        palavra = "oitocentos e " + palavra
    elif numero == 900:
        palavra = "novecentos"
    elif numero < 1000:
        palavra = "novecentos e " + palavra
    elif numero == 1000:
        palavra = "mil"

    letras = palavra.replace(" ", "").replace("-", "")
    total_letras += len(letras)

print(f"O total de letras usadas para escrever os números de 1 a 1000 em palavras é: {total_letras}")
