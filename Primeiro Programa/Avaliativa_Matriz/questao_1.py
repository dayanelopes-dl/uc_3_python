# 1. Crie uma matriz 2x2 contendo os valores: 1, 2, 3, 4 e exiba em tela

matriz = [[1, 2],
         [3, 4]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        
        print(matriz[linha][coluna], end=" ")
        
    print()