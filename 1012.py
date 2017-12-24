linha = input().split(" ")
A, B, C = linha
pi = 3.14159

areaTri = (float(A) * float(C))/2
areaCirculo = (float(C) ** 2) * pi
areaTrap = (float(C) * (float(A) + float(B))/2)
areaQuad = float(B) ** 2
areaRet = (float(A) * float(B))

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" %(areaTri, areaCirculo, areaTrap, areaQuad, areaRet))