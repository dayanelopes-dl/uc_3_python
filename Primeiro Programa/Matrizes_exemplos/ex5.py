
matriz = []
for i in range(3): #esse for é a linha
    linha = [] #linha vazia
    for j in range(3): #esse for é a coluna
        msg = f'numero da celula [{i}][{j}]: ?'
        linha.append(int(input(msg))) #adiciona o numero digitado na linha
    matriz.append(linha) #adiciona a linha na matriz

pares = 0
for linha in matriz:
    for e in linha:
        if e % 2 == 0:
            pares += 1
for linha in matriz:
    print(linha)

print(f"A matriz contem {pares} numeros pares.")
        