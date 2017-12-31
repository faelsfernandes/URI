from math import sqrt
while True:
	try:
		r1, x1, y1, r2, x2, y2 = [float(x) for x in input().split()]
		distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
		print("RICO" if r1 >= distancia + r2 else "MORTO")
	except EOFError:
		break
