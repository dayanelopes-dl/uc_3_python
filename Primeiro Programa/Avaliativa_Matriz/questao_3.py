#3. Solicite ao usuário os valores de uma matriz 3x3. Ao final exiba a matriz completa.

matriz = []

for i in range(3): 
    linha = []   
    for j in range(3): 
        msg = f'valor {j+1} da matriz {i+1}: '
        linha.append(int(input(msg))) 
    matriz.append(linha) 
    
print(f"Valores da Matriz completa: {matriz}")