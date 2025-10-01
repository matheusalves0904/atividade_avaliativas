linha1 = input()
linha2 = input() 
linha3 = input() 
linha4 = input()  

dia_inicio = int(linha1.split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, linha2.split(' : '))

dia_fim = int(linha3.split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, linha4.split(' : '))

segundos_inicio = dia_inicio * 86400 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
segundos_fim = dia_fim * 86400 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim

duracao_total = segundos_fim - segundos_inicio

dias = duracao_total // 86400
duracao_total = duracao_total % 86400

horas = duracao_total // 3600
duracao_total = duracao_total % 3600

minutos = duracao_total // 60
segundos = duracao_total % 60

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")
