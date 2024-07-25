import math

hora_chegada = int(input("Digite a hora de chegada (00-23): "))
minuto_chegada = int(input("Digite os minutos de chegada (00-59): "))
hora_partida = int(input("Digite a hora de partida (00-23): "))
minuto_partida = int(input("Digite os minutos de partida (00-59): "))

taxa_1_2_horas = 1.00
taxa_3_4_horas = 1.40
taxa_5_horas_e_acima = 2.00

if hora_partida < hora_chegada:
    hora_partida += 24

minutos_totais_chegada = hora_chegada * 60 + minuto_chegada
minutos_totais_partida = hora_partida * 60 + minuto_partida

minutos_totais_estacionado = minutos_totais_partida - minutos_totais_chegada

horas_totais_estacionadas = math.ceil(minutos_totais_estacionado / 60)

if horas_totais_estacionadas <= 2:
    valor = horas_totais_estacionadas * taxa_1_2_horas
else:
    if horas_totais_estacionadas <= 4:
        valor = 2 * taxa_1_2_horas + (horas_totais_estacionadas - 2) * taxa_3_4_horas
    else:
        valor = 2 * taxa_1_2_horas + 2 * taxa_3_4_horas + (horas_totais_estacionadas - 4) * taxa_5_horas_e_acima

print(f"O valor do estacionamento é R$ {valor}")
