#Como preencher uma matriz com valores fornecidos pelo usuário:

matriz = []

for linha in range(3): 
    nova = []
    for coluna in range(3):
        valor = float(input(f"Nota: "))
        nova.append(valor)
    matriz.append(nova) 
    
    
#Para imprimir a matriz preenchida e organizada como uma matriz literalmente:
    
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        
        print(matriz[linha][coluna], end= " ")
    print()
   
   