notas = []   #matriz vazia

for i in range(3): # esse for é a linha - 3
    linha = []   # linha vazia
    for j in range(3): # esse for é a coluna - 3
        msg = f'Nota {j+1} do aluno {i+1}: '
        linha.append(float(input(msg))) 
    notas.append(linha) # adiciona a linha na matriz
    
print(notas) # imprime a matriz 