#Faça um programa para leia o horário (hora, minuto e segundo) de início e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma
horas = int(input("Digite a hora de início: "))
min = int(input("Digite o minuto de início: "))
seg = int(input("Digite o segundo de início: "))

duracao = int(input("Digite a duração em segundos: "))

inicio = horas * 3600 + min * 60 + seg
termino = inicio + duracao

hora_t = (termino//3600)
min_t = (termino % 3600) // 60
seg_t = termino % 60


print(f"{hora_t} horas, {min_t} minutos e {seg_t} segundos")