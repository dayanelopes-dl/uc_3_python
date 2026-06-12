#Retorne o maior e o menor valor presente na matriz.

matriz = [
    [12, 5, 8],
    [3, 20, 7],
    [9, 1, 15]
]


maior = matriz[0][0]
menor = matriz[0][0]


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            #print(maior)
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            #print(menor)
            menor = matriz[i][j]

print(f"O maior valor na matriz é: {maior}")
print(f"O menor valor na matriz é: {menor}")