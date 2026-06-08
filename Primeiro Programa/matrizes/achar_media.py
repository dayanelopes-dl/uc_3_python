#Achar a media de cada linha da matriz:

matriz = [
    [1, 2],
    [4, 5]
]


for linha in range(len(matriz)):
    #print(linha)
    soma = 0
    for coluna in range(len(matriz[linha])):
        soma = soma + matriz[linha][coluna]
        
    media = soma / len(matriz[linha])
    print(f"A média da linha {linha} é: {media:.2f}")