#Calcular média da turma usando matriz

notas = [
    [5.0, 4.5, 7.0, 5.2, 6.1], 
    [2.1, 6.5, 8.0, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3]
]

cont = soma = 0

for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(soma)
        print(cont)
        soma = soma + notas[linha][coluna]
        cont = cont + 1
        
media = soma / cont
print(f"A média da turma é: {media:.2f}")