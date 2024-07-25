nota = float(input('Insira a nota: '))
falta = int(input('Insira as faltas: '))

if falta <= 20:
    if 9 <= nota <= 10:
        print('O seu conceito é A')
    elif 7.5 <= nota <= 8.9:
        print('O seu conceito é B')
    elif 5 <= nota <= 7.4:
        print('O seu conceito é C')
    elif 4 <= nota <= 4.9:
        print('O seu conceito é D')
    else:
        print('O seu conceito é E')
    
else:
    if 9 <= nota <= 10:
        print('O seu conceito é B')
    elif 7.5 <= nota <= 8.9:
        print('O seu conceito é C')
    elif 5 <= nota <= 7.4:
        print('O seu conceito é D')
    elif 4 <= nota <= 4.9:
        print('O seu conceito é E')
    else:
        print('O seu conceito é E')