n = int(input("digite a dimensao n da matriz: "))  #sempre é primeiro coluna e depois coulna
m = int(input("digite a dimensao m da matriz: "))

matriz = [] #matriz vazia

for i in range(n): #esse for é a linha
    linha = [] #linha vazia
    for j in range(m): #esse for é a coluna
        linha.append(0)
    matriz.append(linha) #adiciona a linha na matriz

print(matriz) #imprime a matriz