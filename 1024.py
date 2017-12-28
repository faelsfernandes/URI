texto = input()
for i in range(len(texto)):
	texto = list(texto)
	if (texto[i] >= 'a' and texto[i] <= 'z') or (texto[i] >= 'A' and texto[i] <= 'Z'):
		texto[i] = chr(ord(texto[i])+3)

texto.reverse()
	
for i in range(int(len(texto)/2), len(texto)):
			texto[i] = chr(ord(texto[i])-1)	

texto = "".join(texto)
print(texto)