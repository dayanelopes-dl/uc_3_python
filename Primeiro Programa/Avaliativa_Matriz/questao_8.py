# 8. Solicite os valores de uma matriz 4x4 e informe quantos números pares existem. 

matriz = []
for i in range(4):
    linha = [] 
    for j in range(4): 
        msg = f'digite valores da matriz 4x4 [{i}][{j}]: '
        linha.append(int(input(msg))) 
    matriz.append(linha) 

pares = 0
for linha in matriz:
    for e in linha:
        if e % 2 == 0:
            pares += 1
for linha in matriz:
    print(linha)

print(f"A matriz contem {pares} numeros pares.")
        