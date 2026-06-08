#Percorrendo matriz com for:


matriz = [
    [1, 2, 3],    #Linha 0
    [4, 5, 6],    #Linha 1
    [7, 8, 9]     #Linha 2
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        
        print(matriz[linha][coluna], end=" ") #O end=" " serve para imprimir os elementos da mesma linha na mesma linha, ou seja, sem pular para a próxima linha.
        
    print() #Pula para a próxima linha
               