# 6. Solicite os valores de uma matriz 3x3 e exiba apenas os elementos da diagonal principal

matriz = []

for i in range(3): 
    linha = []   
    for j in range(3): 
        msg = f'digite o valor {j+1} da matriz {i+1}: '
        linha.append(float(input(msg)))
    matriz.append(linha) 
print(matriz)

print(f"valores em diagonal : {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")