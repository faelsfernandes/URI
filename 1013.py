linha = input().split(" ")
A, B, C = linha

resultado = (int(A) + int(B) + abs(int (A) - int(B)))/2
resultado = (int (resultado) + int (C) + abs(int (resultado) - int(C)))/2

print("%d eh o maior" %resultado)