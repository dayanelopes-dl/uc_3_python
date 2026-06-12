# 5. Solicite os valores de uma matriz 3x3 e encontre o maior valor

matriz = []

for i in range(3): 
    linha = []   
    for j in range(3): 
        msg = f'digite o valor {j+1} da matriz {i+1}: '
        linha.append(float(input(msg)))
    matriz.append(linha) 

maior = 0 
for i in range(len(matriz)):
    if matriz[i][1] > matriz[maior][1]:
        maior = i

print(f"O maior valor é: {matriz[maior][0]}")