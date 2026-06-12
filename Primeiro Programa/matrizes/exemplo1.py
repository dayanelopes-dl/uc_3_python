'''VETOR = x = [ [], [], [] ] '''


# Acessando matrizes: 

'''matriz = [
    [1, 2, 3],    #Linha 0      
    [4, 5, 6],    #Linha 1
    [7, 8, 9]     #Linha 2
]

print(matriz)

print(matriz[2][1]) #Resultado 8, o numero 2 representa a linha e o numero 1 representa a coluna, ou seja, o numero 8 esta na linha 2 e coluna 1.'''


matriz = [
    [10, 20, 30],    #Linha 0
    [40, 50, 60],    #Linha 1   
]

#Descobrir quantidade de linhas e colunas de uma matriz:

linhas = len(matriz) #Quantidade de linhas
colunas = len(matriz[0]) #Quantidade de colunas

print(f"Linhas: {linhas}")
print(f"Colunas: {colunas}")  