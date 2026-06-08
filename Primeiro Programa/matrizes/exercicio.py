'''Elabore um algoritmo onde solicita para o usuário criar uma matriz N,M.
Solicita para preencher a matriz.
Descobre o maior e menor valor, e apresente os numeros pares dessa matriz.'''

matriz = []

#Solicitar ao usuário a quantidade de linhas e colunas da matriz:

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

#Agora posso utilizar as informações de linhas e colunas para preencher a matriz com os valores fornecidos pelo usuário:
for linha in range(linhas): 
    nova = []
    for coluna in range(colunas):
        valor = float(input(f"Número: "))
        nova.append(valor)
    matriz.append(nova)
    
#Descobrir o maior e menor valor presente na matriz:
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

#Mostrando os números pares da matriz:

print("Números pares na matriz: ")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            print(matriz[i][j], end=" ")
        
        if matriz[i][j] % 2 != 0:
            print(f"Números ímpares na matriz: {matriz[i][j]}", end=" ")
        print()       
    
   