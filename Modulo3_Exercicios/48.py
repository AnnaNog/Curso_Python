#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
segundos = int(input("Digite o valor em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos")
