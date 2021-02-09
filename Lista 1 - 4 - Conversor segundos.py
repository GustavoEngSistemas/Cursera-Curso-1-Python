total_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = total_segundos // 86400
total_segundos = total_segundos % 86400
horas = total_segundos // 3600
total_segundos = total_segundos % 3600
minutos = total_segundos // 60
segundos = total_segundos % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
