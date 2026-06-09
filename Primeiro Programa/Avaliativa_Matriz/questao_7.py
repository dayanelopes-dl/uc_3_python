# 7. Solicite os valores de uma matriz 3x3 e calcule a soma da diagonal principal. 

matriz = []

soma = 0


for i in range(3):
    linha = []
    for j in range(3):
        msg = f'Digite o valor [{j+1}] da linha [{i+1}]: '
        linha.append(float(input(msg)))
    matriz.append(linha)

soma = 0
for i in range(3):
    soma += matriz[i][i]

print(f"valores em diagonal : {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")

print(f"Valor da soma da diagonal principal: {soma}")

 