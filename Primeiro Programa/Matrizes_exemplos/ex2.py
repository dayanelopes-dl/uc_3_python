        #  0 -  1 -  2  - 3  - 4
notas = [[5.0, 4.5, 7.0 ,5.2, 6.1],  #0
         [2.1, 6.5, 5.0, 7.0, 6.7],  #1
         [8.6, 7.0, 9.1, 8.7, 9.3]]  #2      Matriz

cont = soma =  0

for linha in range(len(notas)):   #Percorre as linhas da matriz
    print(f"linhas percorridas: {linha}")
    for coluna in range(len(notas[linha])): #Percorre as colunas da matriz
        print(f"colunas percorridas: {coluna}")
        print(f"Valor da matriz: {notas[linha][coluna]}")
        soma = soma + notas[linha][coluna] #Soma os valores da matriz
        cont = cont + 1 #Contador para contar a quantidade de elementos da matriz

media = soma / cont #Calcula a media dos valores da matriz
print(f" Média das notas: {media}")