# 9. Solicite os valores de uma matriz 3x3 e calcule a média dos elementos. 


matriz = []

cont = soma =  0


for i in range(3):
    linha = []
    for j in range(3):
        msg = f'Digite o valor [{j+1}] da linha [{i+1}]: '
        linha.append(float(input(msg)))
    matriz.append(linha)

    soma = soma + matriz[i][j] 
    cont = cont + 1 

media = soma / cont 
print(f" Média das notas: {media}")