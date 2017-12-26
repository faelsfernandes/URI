segundos = int(input())
auxsegundos = segundos

horas = minutos = 0

horas = int(segundos/3600)
segundos -= horas*3600
	
minutos = int(segundos/60)
segundos -= minutos*60
	
print("%d:%d:%d" %(horas, minutos, segundos))