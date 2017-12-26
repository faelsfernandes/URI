texto = input()
for i in range(len(texto)):
	texto = list(texto)
	if (ord(texto[i]) >= 65 and ord(texto[i]) <= 90) or (ord(texto[i]) >= 97 and ord(texto[i]) <= 122):
		texto[i] = chr(ord(texto[i])+3)

if len(texto) > 1:
	texto.reverse()
	
for i in range(int(len(texto)/2), len(texto)):
			texto[i] = chr(ord(texto[i])-1)	

texto = "".join(texto)
print(texto)