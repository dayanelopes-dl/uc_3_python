#4. Solicite os valores de uma matriz 3x3 e calcule a soma de todos os elementos.

matriz = []

soma = 0 

for i in range(3): 
    linha = []   
    for j in range(3): 
        msg = f'digite o valor {j+1} da matriz {i+1}: '
        linha.append(int(input(msg)))
    matriz.append(linha) 

for i in range(len(matriz)):
    for j in range(len(matriz[1])):
        soma = soma + matriz[i][j]  

print(f"A soma de todos os elementos: {soma}")