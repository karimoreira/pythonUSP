segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos = int(segundos_str)

horas = total_segundos // 3600
segs_restantes = total_segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")
