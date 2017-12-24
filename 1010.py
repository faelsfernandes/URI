linha1 = input().split(" ")
linha2 = input().split(" ")

codP1, qtdP1, valorP1 = linha1
codP2, qtdP2, valorP2 = linha2

total = (int (qtdP1) *float(valorP1)) + (int(qtdP2) * float(valorP2)) 

print("VALOR A PAGAR: R$ %0.2f" %total)